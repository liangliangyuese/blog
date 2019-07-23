# coding=utf-8
import random
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # 随机默认头像
    user_img_default = [
        "/static/image/9ee0cde4dffa4fc780401561ed9d8809.jpeg",
        "/static/image/791e1a3aff021817b4028b1d91b92f80.jpeg",
        "/static/image/2096723084f0ad8784bedc58f039a293.jpeg",
        "/static/image/c0a054d72dddb1df0d22f0bd2956a112.jpeg",
        "/static/image/ca905f2d53a18949c18596c0feb606d5.jpeg",
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=50, unique=True, verbose_name="手机号")
    user_img = models.CharField(max_length=500, verbose_name="用户头像", default=random.choice(user_img_default))

    class Meta:
        verbose_name = "User Profile"
