# coding=utf-8
import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 文章的首页
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/index.html', {"username": u})
    elif request.method == "POST":
        # 查询目标用户的文章数量
        u = request.COOKIES.get("username")
        if u:
            # TODO
            return json.dumps({"code": 200, "message": "成功", "data": 11})
        else:
            return json.dumps({"code": 40003, "message": "请登录"})


def admin(request):
    # 管理文章
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/admin.html', {"username": u})
    elif request.method == "POST":
        u = request.COOKIES.get("username")
        if u:
            return json.dumps({"code": 200, "message": "成功", "data": 11})
        else:
            return json.dumps({"code": 40003, "message": "请登录"})


def write(request):
    # 写文章/修改文章
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/write.html', {"username": u})
    elif request.method == "POST":
        u = request.COOKIES.get("username")
        if u:
            return json.dumps({"code": 200, "message": "成功", "data": 11})
        else:
            return json.dumps({"code": 40003, "message": "请登录"})
