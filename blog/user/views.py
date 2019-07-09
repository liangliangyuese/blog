# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


def index(request):
    # 用户信息首页
    return HttpResponse("hello,this is user info index!")


def register(request):
    if request.method == "GET":
        obj = RegisterForm()
        return render(request, 'user/register.html', {'obj': obj})
    elif request.method == "POST":
        obj = RegisterForm(request.POST)
        print(obj)
        if obj.is_valid():
            print("注册用户成功")
            username = obj.cleaned_data.get("username")
            email = obj.cleaned_data.get("email")
            password1 = obj.cleaned_data.get("password1")
            user = User.objects.create(username=username, email=email, password=password1)
            return HttpResponseRedirect('/user/login/')
        else:
            print("注册用户失败")
            return HttpResponse('提交数据不合法')


def login(request):
    if request.method == "GET":
        obj = LoginForm()
        return render(request, 'user/login.html', {'obj': obj})
    elif request.method == "POST":
        obj = LoginForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data.get("username")
            response = HttpResponse('登录成功')
            response.set_cookie("username", username)
            return response
        else:
            return HttpResponse('登陆失败')
