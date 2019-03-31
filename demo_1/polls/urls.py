#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-3-27 21:44 
# @Author : Mark 
# @Site :  
# @File : urls.py 
# @Software: PyCharm Community Edition
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # 通用视图
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]