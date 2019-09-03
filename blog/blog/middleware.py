# coding=utf-8
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


# TODO 中间件
# 中间件完成后-在setting文件 中间件注册
class LoginMiddleware(MiddlewareMixin):
    # 登录中间件
    def process_request(self, request):
        pass
        # if request.path == '/user/info/':
        #     if request.COOKIES.get("username"):
        #         pass
        #     else:
        #         return HttpResponseRedirect('/user/login/')
        # else:
        #     pass
