# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         urls
# Description:  
# Author:       buer1990
# Date:         2019/1/9
# -------------------------------------------------------------------------------
from django.conf.urls import url

from comments import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
