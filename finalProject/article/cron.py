from django.utils import timezone
from article.ditAPI import tools, modelPredictScore, pred
from article.models import Article

def cronCrawling():
    today = timezone.now()
    print('datilyCrawling 시작 : ', today)
    tests = tools.daily_news_grab()

   # for test in tests:
    test = tests[0]
    print(test)
    model_result = pred.modelPredictFunc(test['title'], test['contents'])
    print(model_result)
    article = Article(title=test["title"], reporter=test["reporter"], press=test["press"], link=test["link"], publication_time=test["time"], crawling_time=today, img=test["img"], result=model_result, gubun='daily')
    print(article)
    article.save()

    print('datilyCrawling 끝 : ', timezone.now())



# def cronCrawling() :
#     print("start gubun : ", timezone.now())
#     # views.datilyCrawling()
#     # print('cronCrawling 함수 실행투 : ', timezone.now())
#     pass
 
