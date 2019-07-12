# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/index.html', {"username": u})


def admin(request):
    # 管理文章
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/admin.html', {"username": u})


def write(request):
    # 写文章/修改文章
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/write.html', {"username": u})
