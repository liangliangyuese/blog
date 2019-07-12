# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", views.admin, name="register"),
    path("write/", views.write, name="register"),
]
