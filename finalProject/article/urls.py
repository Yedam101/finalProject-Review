from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('inputCrawling/', views.InputUrlCrawling),
    path('viewtest/', views.viewtest), # user input article 분석 함수 실행
    path('viewtest2/', views.viewtest2),  # daily 10 articles 분석
    path('newsview/', views.main), # 실질적 main page
    path('newsview/result',views.result, name='result'), # 분석 결과 page
    path('wordcloudtest/', views.wordcloudtest) # wordcloud test용 url
] 