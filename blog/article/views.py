# coding=utf-8
from django.shortcuts import render
from article.models import Article
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ArticleForm, AlterArticleForm


def index(request):
    # 文章的首页
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/index.html', {"username": u})
    elif request.method == "POST":
        # 查询当前登录用户的文章列表（不返回文章内容）
        u = request.COOKIES.get("username")
        if u:
            user = User.objects.filter(username=u).first()
            article = Article.objects.filter(user=user).all()
            data = [
                {"article_id": i.id, "user": i.user, "article_label": i.label, "article_collect": i.collect,
                 "article_like": i.like, "article_title": i.title} for i in article]
            data = {"code": 200, "message": "成功", "data": data}
        else:
            data = {"code": 40003, "message": "请登录"}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def remove(request):
    if request.method == "GET":
        # 删除用户目标文章
        u = request.COOKIES.get("username")
        article_id = request.GET.get("article_id")
        user = User.objects.filter(username=u).first()
        Article.objects.filter(user=user, id=article_id).delete()
        data = {"code": 200, "message": "文章删除成功"}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


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
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'article/hot.html', {"username": u})
    elif request.method == "POST":
        # 默认返回数据库10条文章信息
        res = Article.objects.all()[:10]
        data = [{"label": i.label, "collect": i.collect, "like": i.like, "title": i.title, "content": i.content,
                 "user": i.user} for i in res]
        data = {"code": 200, "message": "获取文章信息成功", "data": data}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def alter(request):
    if request.method == "GET":
        # 编辑文章页面
        u = request.COOKIES.get("username")
        return render(request, 'article/alter.html', {"username": u})
    elif request.method == "POST":
        obj = AlterArticleForm(request.POST)
        if obj.is_valid():
            id = obj.cleaned_data.get('id')
            title = obj.cleaned_data.get('title')
            label = obj.cleaned_data.get('label')
            content = obj.cleaned_data.get('content')
            Article.objects.filter(id=id).update({"title": title, "content": content, "label": label})
            return JsonResponse({"code": "200", "message": "文章编辑成功"}, safe=False,
                                json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"code": "40005", "message": "文章编辑失败"}, safe=False,
                                json_dumps_params={'ensure_ascii': False})
