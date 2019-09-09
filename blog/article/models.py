# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=20, verbose_name="文章标签")
    collect = models.IntegerField(verbose_name="文章收藏数量")
    like = models.IntegerField(verbose_name="文章点赞数量")
    title = models.CharField(max_length=20, verbose_name="文章标题")
    content = MDTextField(default="ok,现在开始编写你的内容吧！", verbose_name="文章内容")
    # content = models.TextField(verbose_name="文章正文")


class ArticleState(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="目标文章id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="操作用户的id")
    like_state = models.BooleanField(verbose_name="喜欢的状态")
    collect_state = models.BooleanField(verbose_name="收藏的状态")

    # 文章 点赞/收藏 的数量在属性发生变化后根据属性的变化自动更新
    # 自动计算文章新的
    @classmethod
    def like(cls, article_id, user_id, status):
        # 修改喜欢的状态
        ArticleState.objects.filter(article_id=article_id, user_id=user_id).update({"like_state": status})

    @classmethod
    def collect(cls, article_id, user_id, status):
        # 修改收藏的状态
        ArticleState.objects.filter(article_id=article_id, user_id=user_id).update({"collect_state": status})

    @classmethod
    def amount(cls, article_id, like=None, collect=None):
        if like:
            # 汇总目标文章 like数量
            number = ArticleState.objects.filter(article_id=article_id, like_state=1).count()
            Article.objects.filter(id=article_id).update({"like": number})
        if collect:
            # 汇总目标文章
            number = ArticleState.objects.filter(article_id=article_id, collect_state=1).count()
            Article.objects.filter(id=article_id).update({"collect":number})


# markdown 测试模型
class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField(default="ok,现在开始编写你的内容吧！")
