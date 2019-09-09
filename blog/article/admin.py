# coding=utf-8
from django.contrib import admin
from .models import ExampleModel

# Register your models here.
# 注册model- 注册原因？？？ 用途
admin.site.register(ExampleModel)
