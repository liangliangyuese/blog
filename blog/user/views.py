# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 用户信息首页
    return HttpResponse("hello word,this is user index!")


def register(request):
    pass


def login(request):
    pass
