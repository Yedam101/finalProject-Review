from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from article.ditAPI import tools, modelPredictScore, pred, wordcloud # ㅇㅖ담님 짱 good
import json
from django.utils import timezone
from article.models import Article
from django.http import JsonResponse
from django.db.models import Q

import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static



# ------------------------- Don't touch Code


def index(request):
    return HttpResponse("서버연결 극혐2")

# url to Crawling
def InputUrlCrawling(inputUrl):
    temp = tools.get_title_contents(inputUrl)
    today = timezone.now()
    print('input temp : ', temp)


    # titleulr = Article.objects.filter(articleid__gt=1).values('title', 'link')
    # print('titleulr : ', titleulr)
    # 제목temp["title"]과 링크inputUrl DB에 있는 데이터 조회해서 
    # 같은 값 있는지 체크
    # 있으면 그 데이터 그대로 리턴
    # 없으면 세이브

    same = Article.objects.filter(Q(title=temp['title']) & Q(link=inputUrl) & Q(gubun='input'))
    if same:
        return same

    result = pred.modelPredictFunc(temp['title'], temp['contents'])# 예측 
    print('input result : ', result)
    article = Article(title=temp["title"], reporter=temp["reporter"], press=temp["press"], link=inputUrl, publication_time=temp["time"], crawling_time=today, img=temp["img"], result=result, gubun='input')
    print(article.title)
    
    article.save() # 데이터 저장 실질적인 데이터 테스트 완료 후 주석 풀기
    wordcloud.Wordcloud(temp['contents'], article.articleid) 
    
    return article



    
    # result = pred.modelPredictFunc(temp['title'], temp['contents'])# 예측 
    # print('input result : ', result)
    # article = Article(title=temp["title"], reporter=temp["reporter"], press=temp["press"], link=inputUrl, publication_time=temp["time"], crawling_time=today, img=temp["img"], result=result, gubun='input')
    # print(article.title)
    
    # article.save() # 데이터 저장 실질적인 데이터 테스트 완료 후 주석 풀기

    # wordcloud.Wordcloud(temp['contents'], article.articleid) 

    # return article



# 예측 
def modelPredict(article) :
    '''
    점수? binary ?  일관성이 있을 확률  ex)0.72
    '''
    return modelPredictScore.articleScore(article)

# datily Crawling 
def datilyCrawling():

    '''
    1. tools의 데일리크롤링한 함수 호출 (return값 딕셔너리 열개 담긴 리스트 하나로 옴)
    2. 리스트 loop moon
    3. 저 안에서 하나씩 예측하기 예측함수 호출
    4. DB에 담기
    5. 로그 쌓기 시작할 때 한 번 하고 하나씩 담길 때 하고 끝날 때 한번

    '''
    print('daily crawling start')
    today = timezone.now()
    tests = tools.daily_news_grab()

    for test in tests:
        print(test)
        model_result = pred.modelPredictFunc(test['title'], test['contents'])
        print(model_result)
        article = Article(title=test["title"], reporter=test["reporter"], press=test["press"], link=test["link"], publication_time=test["time"], crawling_time=today, img=test["img"], result=model_result, gubun='daily', logo=test["logo"], thumbnail=test["thumbnail"], category=test["category"])
        print(article)
        article.save()

        wordcloud.Wordcloud(test['contents'], article.articleid)

    print('datilyCrawling 함수 실행 : ', timezone.now())



def viewtest(request) :
    # 화면 가져가는 데이터
    # 화면에서 input 받은 데이터

    temp = InputUrlCrawling("https://n.news.naver.com/article/024/0000078382?cds=news_media_pc&type=editn")
    print('Input result : ', temp)

    # json_val = json.dumps(data, ensure_ascii=False).encode('utf8') 
    return HttpResponse(temp)



def viewtest2(request) :
    # texts = tools.get_title_contents("https://n.news.naver.com/article/648/0000011744?cds=news_media_pc&type=editn")
    # text = texts["contents"] # 내용 값만 변수에 저장
    # uri = wordcloud.Wordcloud(text) # 이미지 리턴
    # print(len(uri))

    # return HttpResponse(uri)
    # # return render(request, 'wordcloudgen/cloud_gen.html', uri) # test용 http 따로 만듦. 
    # # return HttpResponse('test2')
    datilyCrawling()

    return HttpResponse('gg')








def wordcloudtest(request):
    texts = tools.get_title_contents("https://n.news.naver.com/article/648/0000011744?cds=news_media_pc&type=editn")
    text = texts["contents"] # 내용 값만 변수에 저장
    b64 = wordcloud.Wordcloud(text, '아무값' ) # 이미지 리턴
    print(b64)
    context = {'img': b64}
    render(request, 'hello/temp.html', context)

    # wc = WordCloud(width=400, height=400, scale=2.0, max_font_size=250, font_path="C:/venvs/final/wslFinal/finalProject/article/ditAPI/BMDOHYEON_ttf.ttf")
    # gen = wc.generate_from_frequencies(c)
    # plt.figure()
    # plt.imshow(gen)
    # args = {'image': plt.imshow(gen)}
    # print(len(uri))

    # render(request, 'hello/temp.html', args)



# ------- 아래부터 함수 추가하시면 됩니다. 

from django.template import loader
from django.http import JsonResponse
def main (request):
    articles=Article.objects.filter(gubun="daily").order_by('-crawling_time')[:10]
    template=loader.get_template('article/mainpage.html')
    for i in articles:
        i.category_news=tools.category_news_grab(i.category)
    
    context={
        "articles":articles,
    }
    
    return HttpResponse(template.render(context,request))

def result(request):
    from datetime import datetime
    link=request.GET.get('inputLink')
    if Article.objects.filter(link=link):
        article=Article.objects.get(link=link)
        time=article.publication_time.strftime("%Y/%m/%d %H:%M:%S")
        news = {
            'id':article.articleid,
            'title':article.title,
            'reporter':article.reporter,
            'press': article.press,
            'result': article.result,
            'img':article.img,
            'time':time
            }
    else:
        article=InputUrlCrawling(link)
        time=article.publication_time.strftime("%Y/%m/%d %H:%M:%S")
        news= {
            'id':article.articleid,
            'title':article.title,
            'reporter':article.reporter,
            'press': article.press,
            'result': article.result,
            'img':article.img,
            'time':time
            }
    return JsonResponse(news)