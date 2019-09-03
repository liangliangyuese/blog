# coding=utf-8
from django import forms
from django.contrib.auth.models import User


def email_check(email):
    # 邮箱检查
    pass


def phone_check(phone):
    # 手机号检查
    pass


class RegisterForm(forms.Form):
    # 注册表单
    username = forms.CharField(label="用户昵称", max_length=50)
    email = forms.EmailField(label="用户邮箱")
    password1 = forms.CharField(label="用户密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) > 10:
            raise forms.ValidationError("用户昵称长度必须小于10")
        filter_result = User.objects.filter(username=username)
        if len(filter_result):
            raise forms.ValidationError("你注册的用户昵称已经存在了")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        filter_result = User.objects.filter(email=email)
        if len(filter_result):
            raise forms.ValidationError("用户邮箱 已经存在")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 6:
            raise forms.ValidationError("密码过短，密码6-20位")
        elif len(password1) >= 20:
            raise forms.ValidationError("密码过长，密码6-20位")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return password2


class LoginForm(forms.Form):
    # 登陆表单
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username=username)
        if not filter_result:
            raise forms.ValidationError("用户不存在")
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")
        filter_result = User.objects.filter(username=username, password=password)
        if not filter_result:
            raise forms.ValidationError("密码不匹配")
        return password


class RestForm(forms.Form):
    # 重置密码表单
    password1 = forms.CharField(label="用户密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 6:
            raise forms.ValidationError("密码过短，密码6-20位")
        elif len(password1) >= 20:
            raise forms.ValidationError("密码过长，密码6-20位")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return password2
