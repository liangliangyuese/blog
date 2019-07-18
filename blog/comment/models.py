# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from blog.question.models import Question


# 用户私信
class UserComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户私信id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    comment_time = models.DateTimeField(verbose_name="私信时间")
    comment_content = models.TextField(verbose_name="私信正文")


class UserCommentBack(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户私信回复id")
    user_comment = models.ForeignKey(UserComment, on_delete=models.CASCADE, verbose_name="用户评论外键关联")


# 文章

# 问答评论
class QuestionComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="问答回复id")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问答外键关联")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    reply_time = models.DateTimeField(verbose_name="回复时间")
    reply_content = models.TextField(verbose_name="提问正文")


# 问答评论回复
class QuestionUserComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="问答用户回复id")
    question_comment = models.ForeignKey(QuestionComment, on_delete=models.CASCADE, verbose_name="问答回复外键关联")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    reply_time = models.DateTimeField(verbose_name="回复时间")
    reply_content = models.TextField(verbose_name="提问正文")

# 评论id
# 帖子id
# 用户id
# 回复内容
# 时间
# 评论上级id
