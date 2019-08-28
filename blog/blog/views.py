# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'blog/index.html', {"username": u})


def introduce(request):
    if request.method == "GET":
        return render(request, 'other/introduce.html')


def bird(request):
    if request.method == "GET":
        return render(request, 'other/bird.html')


def auto_change(request):
    if request.method == "GET":
        return render(request, 'other/auto_change.html')


# 自定义404错误
def page_ont_found(request):
    return render(request, 'error/404.html')


# 自定义403错误
def page_permission_denied(request):
    return render(request, 'error/403.html')


# 自定义500错误页面
def page_error(request):
    return render(request, 'error/500.html')
