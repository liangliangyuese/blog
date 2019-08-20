# coding=utf-8
import json
from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse, JsonResponse


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


def hot(request):
    # 热门文章
    # 当前取数据库中的前十条--》按照点赞排行---》热度计算 增加时间区间
    if request.method == "GET":
        res = Article.objects.all()[:10]
        print(res)
        # TODO 文章作者信息
        # data = [{"label": i.label, "collect": i.collect, "like": i.like, "title": i.title, "content": i.content} for i
        #         in res]
        data = [{"label": "sasd", "collect": "sasd", "like": "sasd", "title": "sasd", "content": "sasd"}]
        data = {"code": 200, "message": "获取文章信息成功", "data": data}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
