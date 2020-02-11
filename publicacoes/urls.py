from django.urls import path

from publicacoes import views

urlpatterns = [
    path('', views.index,name='index'),
    path('tweet/<int:tweet_id>/like/', views.like, name='like'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('tweet/add/', views.tweet_add, name='tweet_add'),
]
