from django.db import models


class Article(models.Model):

    articleid = models.AutoField(primary_key=True) # pk
    title = models.TextField()  # 기사제목
    reporter = models.CharField(max_length=50)  # 기자
    press = models.CharField(max_length=50)  # 언론사
    link = models.URLField()  # 기사링크
    publication_time = models.DateTimeField()  # 발행시간
    publication_str = models.TextField()  # 발행시간 문자열
    result = models.TextField()  # 낚시성인지 결과
    crawling_time = models.DateTimeField()  # 크롤링한 시간
    img = models.TextField() # 기사내부 이미지 
    gubun = models.TextField() # input, daily 구분
    logo = models.TextField() #logo 로고 이미지.
    thumbnail = models.TextField() #thumbnail img 링크
    category= models.TextField() #category 뉴스 분야
    wcpath = models.TextField() # 워드클라우드 이미지 경로
    


    def __str__(self):
        return self.title


