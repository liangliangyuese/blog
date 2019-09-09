# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    # 文章首页
    path("", views.index, name="index"),
    # 管理文章
    path("admin/", views.admin, name="admin"),
    # 新建文章
    path("write/", views.write, name="write"),
]
