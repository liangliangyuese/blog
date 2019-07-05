# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=50, unique=True, verbose_name="手机号")

    class Meta:
        verbose_name = "User Profile"
