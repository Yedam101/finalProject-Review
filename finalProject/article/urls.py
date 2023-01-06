from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('inputCrawling/', views.InputUrlCrawling),
    path('viewtest/', views.viewtest), 
    path('viewtest2/', views.viewtest2), 
    path('newsview/', views.main),
    path('newsview/result',views.result, name='result'),
    path('wordcloudtest/', views.wordcloudtest)
]