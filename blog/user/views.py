# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegisterForm, LoginForm, RestForm


def index(request):
    # 用户信息（页面+接口）
    if request.method == "GET":
        # 用户信息页面
        u = request.COOKIES.get("username")
        return render(request, 'user/info.html', {"username": u})
    elif request.method == "POST":
        # TODO 用户扩展信息现在是在查询用户信息时添加
        # 查找 返回指定用户信息
        # username参数存在认为查找指定用户信息
        username = request.POST.get("username")
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


def register(request):
    # 用户注册（页面+接口）
    if request.method == "GET":
        # 用户注册页面
        u = request.COOKIES.get("username")
        obj = RegisterForm()
        return render(request, 'user/register.html', {'obj': obj, "username": u})
    elif request.method == "POST":
        # 用户信息
        obj = RegisterForm(request.POST)
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
    # 用户登录（页面+接口）
    if request.method == "GET":
        u = request.COOKIES.get("username")
        obj = LoginForm()
        return render(request, 'user/login.html', {'obj': obj, "username": u})
    elif request.method == "POST":
        obj = LoginForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data.get("username")
            password = obj.cleaned_data.get("password")
            user = User.objects.filter(username=username, password=password)
            if user:
                response = HttpResponseRedirect('/')
                response.set_cookie("username", username)
                return response
            else:
                return HttpResponse('账号密码不匹配，登陆失败')
        else:
            return HttpResponse('输入的账号/密码 不符合规范，登陆失败')


def reset(request):
    # 重置密码
    if request.method == "GET":
        u = request.COOKIES.get("username")
        obj = RestForm()
        return render(request, 'user/reset.html', {'obj': obj, "username": u})
    elif request.method == "POST":
        u = request.COOKIES.get("username")
        obj = RestForm(request.POST)
        if obj.is_valid():
            password1 = obj.cleaned_data.get('password1')
            User.objects.filter(username=u).update({'password': password1})
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('重置密码失败')


def logout(request):
    # 用户退出（接口）
    if request.method == "GET":
        # 用户退出 清除cookie，重定向至首页
        response = HttpResponseRedirect('/')
        response.delete_cookie('username')
        return response
