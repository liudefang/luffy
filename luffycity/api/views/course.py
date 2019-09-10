# -*- encoding: utf-8 -*-
# @Time    : 2019-09-09 17:43
# @Author  : mike.liu
# @File    : course.py

from rest_framework.response import Response
from rest_framework.views import APIView


class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        ret = {
            'code': 0,
            'data': [
                {"id": 1, "title": 'python全栈'},
                {"id": 2, "title": 'linux运维'},
                {"id": 3, "title": '金融分析'},
            ]
        }

        return Response(ret)


