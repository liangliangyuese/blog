# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import UserProfile


def index(request):
    # 用户信息首页
    return HttpResponse("hello,this is user info index!")


def register(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        obj = RegisterForm()
        return render(request, 'user/register.html', {'obj': obj, "username": u})
    elif request.method == "POST":
        obj = RegisterForm(request.POST)
        print(obj)
        if obj.is_valid():
            username = obj.cleaned_data.get("username")
            email = obj.cleaned_data.get("email")
            password1 = obj.cleaned_data.get("password1")
            User.objects.create(username=username, email=email, password=password1)
            return HttpResponseRedirect('/user/login/')
        else:
            print("注册失败")
            return HttpResponse('提交数据不合法')


def login(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        obj = LoginForm()
        return render(request, 'user/login.html', {'obj': obj, "username": u})
    elif request.method == "POST":
        obj = LoginForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data.get("username")
            response = HttpResponseRedirect('/')
            response.set_cookie("username", username)
            return response
        else:
            return HttpResponse('登陆失败')


def info(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'user/info.html', {"username": u})
    elif request.method == "POST":
        # 返回用户个人信息
        # TODO 指定用户的个人信息
        # TODO 前端post请求方式优化
        # TODO django csrf 调取首先需要获取对应的
        print("后台接收到post请求")
        username = request.COOKIES.get("username")
        u = User.objects.filter(username=username).first()
        print(u)
        u_info = UserProfile.objects.filter(user=u).first()
        print(u_info)
        return HttpResponse('查询当前登录用户的个人信息')



def logout(request):
    if request.method == "GET":
        response = HttpResponseRedirect('/')
        response.delete_cookie('username')
        return response
