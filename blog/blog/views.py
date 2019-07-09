# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "GET":
        u = request.COOKIES.get("username")
        return render(request, 'blog/index.html', {"username": u})
