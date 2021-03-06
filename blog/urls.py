# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         urls
# Description:  
# Author:       buer1990
# Date:         2018/12/20
# -------------------------------------------------------------------------------

from django.conf.urls import url
from . import views

"""
        比如说我们本地开发服务器的域名是 http://127.0.0.1:8000，
        那么当用户输入网址 http://127.0.0.1:8000 后，Django 
        首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，
        此时只剩下一个空字符串，而 r'^$' 的模式正是匹配一个空字符串
        （这个正则表达式的意思是以空字符串开头且以空字符串结尾），
        于是二者匹配，Django 便会调用其对应的 views.index 函数
"""
# 通过 app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesViews.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^search/$', views.search, name='search'),
]
