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
    username = forms.CharField(label="Username", max_length=50)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) < 6:
            raise forms.ValidationError("你的username长度必须大于6")
        elif len(username) > 50:
            raise forms.ValidationError("你的username长度必须小于50")
        else:
            # TODO username_exact
            filter_result = User.objects.filter(username_exact=username)
            if len(filter_result):
                # TODO raise
                raise forms.ValidationError("你注册的username已经存在了")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        filter_result = User.objects.filter(email_exact=email)
        if len(filter_result):
            raise forms.ValidationError("email 已经存在")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 6:
            raise forms.ValidationError("密码过短")
        elif len(password1) > 20:
            raise forms.ValidationError("密码过长")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(email__exact=username)
        if not filter_result:
            raise forms.ValidationError("邮箱不存在")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError("用户昵称不存在")
        return username


class RestForm(forms.Form):
    # 重置密码
    pass
