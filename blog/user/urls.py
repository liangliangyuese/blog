# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    # 用户首页
    path("", views.index, name="index"),
    # 用户注册
    path("register/", views.register, name="register"),
    # 用户登录
    path("login/", views.login, name="login"),
    # 用户退出
    path("logout/", views.logout, name="logout"),
    # 重置密码
    path("reset/", views.reset, name="reset"),
]
