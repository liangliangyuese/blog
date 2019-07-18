# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=20, verbose_name="文章标签")
    collect = models.IntegerField(verbose_name="文章收藏数量")
    like = models.IntegerField(verbose_name="文章点赞数量")
    title = models.CharField(max_length=20, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章正文")


class ArticleState(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="目标文章id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="操作用户的id")
    like_state = models.BooleanField(verbose_name="喜欢的状态")
    collect_state = models.BooleanField(verbose_name="收藏的状态")

    def like(self, status):
        # 修改喜欢的状态
        pass

    def collect(self, status):
        # 修改收藏的状态
        pass

    def amount(self):
        # 调整对应属性的数量
        pass
