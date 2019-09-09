# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    # 提问详情页面
    path("", views.index, name="index"),
    # 创建提问页面
    path("create/", views.create, name="create"),
    # 编辑问题页面
    path("alter/", views.alter, name="alter"),
]
