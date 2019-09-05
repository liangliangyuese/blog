# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# 帖子属于-
# 谁回答了
# 楼层

class Question(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="提问id")
    title = models.CharField(max_length=20, verbose_name="问题名称")
    content = models.TextField(verbose_name="提问正文")
    start_time = models.DateTimeField(verbose_name="提问时间")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.IntegerField(verbose_name="阅读数量")

    # TODO 方法 函数方法计算 提问新阅读量(被动增加+主动增加)
