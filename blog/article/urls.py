# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", views.admin, name="admin"),
    path("write/", views.write, name="write"),
    path("hot/", views.hot, name="hot"),
]
