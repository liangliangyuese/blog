# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


# 帖子属于-
# 谁回答了
# 楼层

class Question(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="提问id")
    title = models.CharField(max_length=20, verbose_name="问题名称")
    content = MDTextField(default="开始写出你疑惑的问题吧！", verbose_name="提问正文")
    # content = models.TextField(verbose_name="提问正文")
    start_time = models.DateTimeField(verbose_name="提问时间")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.IntegerField(verbose_name="阅读数量", default=0)

    @classmethod
    def amount(cls, question_id):
        # 目标文章阅读数量+1
        now_number = Question.objects.filter(id=question_id).first().read
        Question.objects.filter(id=question_id).update({"read": now_number + 1})
