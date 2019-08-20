# coding=utf-8
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


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
