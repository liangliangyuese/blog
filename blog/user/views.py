# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from .models import UserProfile


# TODO 登录部分目前使用中间件拦截--部分功能修改成装饰器拦截
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
        username = request.COOKIES.get("username")
        u = User.objects.filter(username=username).first()
        data = {"email": u.email, "username": username}
        u_info = UserProfile.objects.filter(user=u).first()
        if u_info:
            # 返回用户的相关信息
            data2 = {"phone": u_info.phone, "user_img": u_info.user_img}
        else:
            # 在用户信息扩展表，生成默认的用户扩展信息
            UserProfile.objects.create(user=u)
            u_info = UserProfile.objects.filter(user=u).first()
            data2 = {"phone": u_info.phone, "user_img": u_info.user_img}
        data.update(data2)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def logout(request):
    if request.method == "GET":
        response = HttpResponseRedirect('/')
        response.delete_cookie('username')
        return response
