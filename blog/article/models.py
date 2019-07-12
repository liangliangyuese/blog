from django.db import models
from django.contrib.auth.models import User


# 作者
# 关注
# 点赞
# 评论
# 喜欢

# 用户-喜欢 多对多  发生变化后-计算新的汇总更新到注意
# 正文如何分割

# 如何判断一个用户只能点赞一次
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(verbose_name="点赞数量")




