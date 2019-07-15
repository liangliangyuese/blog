from django.db import models
from django.contrib.auth.models import User


# 作者
# 关注
# 点赞
# 评论
# 喜欢
# 分类标签

# 用户-喜欢 多对多
# 正文如何分割

# 如何判断一个用户只能点赞一次（多对多查询）
# 如何及时处理新的变化-更新最新点赞/收藏数量
# 文章的分类（文章需要一个或者多个标签）
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=60, verbose_name="文章标签")
    collect = models.IntegerField(verbose_name="文章收藏数量")
    like = models.IntegerField(verbose_name="文章点赞数量")
    title = models.CharField(max_length=60, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章正文")


class ArticleState(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    # 文章id, 操作用户id，收藏状态，喜欢状态
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="目标文章id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="操作用户的id")
    like_state = models.BooleanField(verbose_name="喜欢的状态")
    collect_state = models.BooleanField(verbose_name="收藏的状态")
