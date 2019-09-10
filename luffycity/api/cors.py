# -*- encoding: utf-8 -*-
# @Time    : 2019-09-09 20:13
# @Author  : mike.liu
# @File    : cors.py

from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 允许你的域名来访问
        response['Access-Control-Allow-Origin'] = "*"
        # 允许你携带 Content-Type 请求头 不能写*
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        # 允许你发送 DELETE PUT请求
        response['Access-Control-Allow-Methods'] = 'DELETE,PUT'
        return response
