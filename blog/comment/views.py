# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


# 评论文章（接口）
# 回复文章评论（接口）

# 解答提问（接口）
# 回复解答提问（接口）

# 私信用户（接口）
# 回复用户私信（接口）
def index(request):
    return HttpResponse("hello word,this is comment index!")
