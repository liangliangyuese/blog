# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from question.models import Question


# 用户私信
class UserComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户私信id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id", related_name="目标用户id")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发送私信用户id", related_name="发送用户id")
    comment_time = models.DateTimeField(verbose_name="私信时间")
    comment_content = models.TextField(verbose_name="私信正文")


# 用户私信回复
class UserCommentReply(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="用户私信回复id")
    reply_id = models.CharField(max_length=20, verbose_name="回复id，当reply_id存在时，相当于用户在回复对别人的回复")
    comment_id = models.ForeignKey(UserComment, on_delete=models.CASCADE, verbose_name="评论id")
    comment_content = models.TextField(verbose_name="私信正文")
    comment_time = models.DateTimeField(verbose_name="回复时间")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="回复用户id", related_name="用户私信来源用户id")
    to_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="目标用户id", related_name="用户私信目标用户id")


# 文章评论
class ArticleComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="文章评论id")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章外键关联")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    comment_content = models.TextField(verbose_name="私信正文")
    comment_time = models.DateTimeField(verbose_name="回复时间")


# 文章评论回复
class ArticleCommentReply(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="文章评论回复id")
    reply_id = models.CharField(max_length=20, verbose_name="回复id，当reply_id存在时，相当于用户在回复对别人的回复")
    comment_id = models.ForeignKey(ArticleComment, on_delete=models.CASCADE, verbose_name="评论id")
    comment_content = models.TextField(verbose_name="评论内容")
    comment_time = models.DateTimeField(verbose_name="回复时间")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="回复用户id", related_name="文章来源用户id")
    to_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="目标用户id", related_name="文章目标用户id")


# 问答评论
class QuestionComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="问答回复id")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="问答外键关联")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    comment_content = models.TextField(verbose_name="私信正文")
    comment_time = models.DateTimeField(verbose_name="回复时间")


# 问答评论回复
class QuestionCommentReply(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="问答用户回复id")
    reply_id = models.CharField(max_length=20, verbose_name="回复id，当reply_id存在时，相当于用户在回复对别人的回复")
    comment_id = models.ForeignKey(QuestionComment, on_delete=models.CASCADE, verbose_name="评论id")
    comment_content = models.TextField(verbose_name="评论内容")
    comment_time = models.DateTimeField(verbose_name="回复时间")
    from_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="回复用户id", related_name="问答来源用户id")
    to_uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="目标用户id", related_name="问答目标用户id")
