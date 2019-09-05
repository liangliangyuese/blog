# coding=utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Question
from .forms import CreateQuestionForm, AlterQuestionForm, RemoveQuestionForm


def index(request):
    if request.method == "GET":
        # 提问详情页面
        u = request.COOKIES.get("username")
        return render(request, 'question/index.html', {"username": u})
    elif request.method == "POST":
        # 返回指定用户 提问列表
        username = request.POST.get("username")
        u = User.objects.filter(username=username).first()
        question = Question.objects.filter(user=u).all()
        data = [{"title": i.title, "content": i.content, "id": i.id, "start_time": i.start_time, "read": i.read} for i
                in question]
        data = {"data": data, "code": "200"}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def create(request):
    if request.method == "GET":
        # 创建提问页面
        u = request.COOKIES.get("username")
        return render(request, 'question/create.html', {"username": u})
    elif request.method == "POST":
        # 创建提问接口
        obj = CreateQuestionForm(request.POST)
        if obj.is_valid():
            title = obj.cleaned_data.get("title")
            content = obj.cleaned_data.get("content")
            Question.objects.create(title=title, content=content)
            return HttpResponseRedirect('/question/index/')
        else:
            print("创建新提问")
            return HttpResponse('创建新提问')


def alter(request):
    if request.method == "GET":
        # 编辑问题页面
        u = request.COOKIES.get("username")
        return render(request, 'question/alter.html', {"username": u})
    elif request.method == "POST":
        obj = AlterQuestionForm(request.POST)
        if obj.is_valid():
            id = obj.cleaned_data.get('id')
            title = obj.cleaned_data.get('title')
            content = obj.cleaned_data.get('content')
            Question.objects.filter(id=id).update({"title": title, "content": content})
            return JsonResponse({"code": "200", "message": "文章编辑成功"}, safe=False,
                                json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"code": "40005", "message": "文章编辑失败"}, safe=False,
                                json_dumps_params={'ensure_ascii': False})


def remove(request):
    if request.method == "POST":
        # 删除问题接口
        u = request.COOKIES.get("username")
        u_id = User.objects.filter(username=u).first().id
        obj = RemoveQuestionForm(request.POST)
        if obj.is_valid():
            id = obj.cleaned_data.get('id')
            user = obj.cleaned_data.get('user')
            if user == u_id:
                # 删除文章
                Question.objects.filter(id=id).delete()
                return JsonResponse({"code": "200", "message": "文章删除成功"}, safe=False,
                                    json_dumps_params={'ensure_ascii': False})
            else:
                # 无法删除文章
                return JsonResponse({"code": "40005", "message": "删除文章失败，权限不足"}, safe=False,
                                    json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({"code": "40005", "message": "删除文章失败，传递参数不合法"}, safe=False,
                                json_dumps_params={'ensure_ascii': False})


def hot(request):
    # 热门提问 （接口）
    if request.method == "POST":
        res = Question.objects.all()[:10]
        data = [{"id": i.id, "title": i.title, "content": i.content, "start_time": i.start_time, "user": i.user,
                 "read": i.read} for i in res]
        data = {"code": 200, "message": "获取提问信息成功", "data": data}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
