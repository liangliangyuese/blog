# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


# TODO 评论模块延后
def index(request):
    if request.method == "GET":
        return HttpResponse("hello word,this is comment index!")


def article_comment(request):
    # 评论文章（接口）
    if request.method == "POST":
        pass


def article_comment_reply(request):
    # 回复文章评论（接口）
    if request.method == "POST":
        pass


def question_comment(request):
    # 解答提问（接口）
    if request.method == "POST":
        pass


def question_comment_reply(request):
    # 回复解答提问（接口）
    if request.method == "POST":
        pass


def user_comment(request):
    if request.method == "POST":
        # 私信用户（接口）
        pass


def user_comment_reply(request):
    if request.method == "POST":
        # 回复用户私信（接口）
        pass
