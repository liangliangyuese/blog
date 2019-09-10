# coding=utf-8
from django import forms


class CreateQuestionForm(forms.Form):
    # 提问表单
    # TODO 调整为markdown编辑器
    title = forms.CharField(label="提问标题", max_length=20)
    content = forms.CharField(label="提问正文")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 20:
            raise forms.ValidationError("提问标题的长度要短于20")
        return title


class AlterQuestionForm(forms.Form):
    # 编辑提问表单
    title = forms.CharField(label="提问标题", max_length=20)
    content = forms.CharField(label="提问正文")
    id = forms.IntegerField(label="提问id")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 20:
            raise forms.ValidationError("提问标题的长度要短于20")
        return title


class RemoveQuestionForm(forms.Form):
    # 删除 提问表单
    user = forms.IntegerField(label="用户外键关联")
    id = forms.IntegerField(label="提问id")
