# coding=utf-8
import json
from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ArticleForm


# 1.写文章（页面+接口）
# 2.修改文章（页面+接口）
# 3.删除文章（页面+接口/）

# 4.文章列表（自己的文章）
# 5.当前热门文章（所有人的文章）

# TODO 文章在页面上如何写（from 表单？）
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
        obj = ArticleForm()
        return render(request, 'article/write.html', {"username": u, 'obj': obj})
    elif request.method == "POST":
        user_name = request.COOKIES.get("username")
        obj = ArticleForm(request.POST)
        if obj.is_valid():
            title = obj.cleaned_data.get('title')
            label = obj.cleaned_data.get('label')
            content = obj.cleaned_data.get('content')
            Article.objects.create(collect=0, like=0, label=label, title=title, content=content,
                                   user=User.objects.filter(username=user_name).first())
            return HttpResponseRedirect('/article/admin/')
        else:
            return HttpResponse('文章内容错误')


def hot(request):
    # 热门文章
    # 当前取数据库中的前十条--》按照点赞排行---》热度计算 增加时间区间
    if request.method == "GET":
        res = Article.objects.all()[:10]
        print(res)
        # TODO 文章作者信息
        data = [{"label": i.label, "collect": i.collect, "like": i.like, "title": i.title, "content": i.content} for i
                in res]
        data = {"code": 200, "message": "获取文章信息成功", "data": data}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
