# -*- encoding: utf-8 -*-
# @Time    : 2019-09-09 17:41
# @Author  : mike.liu
# @File    : urls.py.py
from django.conf.urls import url

from api.views import course

urlpatterns = [
    url(r'^course/$', course.CourseView.as_view()),
]