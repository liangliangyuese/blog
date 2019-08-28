# coding=utf-8
from django import forms
from .models import Article, ArticleState


# TODO 标签可以生成新的标签
# TODO 标签可以选择用户现有
class ArticleForm(forms.Form):
    title = forms.CharField(label="文章标题", max_length=20)
    label = forms.CharField(label="文章标签", max_length=20)
    content = forms.CharField(label="文章内容")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 6:
            raise forms.ValidationError("标题长度需要大于6")
        elif len(title) > 20:
            raise forms.ValidationError("标题长度需要小于20")
        else:
            return title

    def clean_label(self):
        label = self.cleaned_data.get("label")
        if len(label) < 6:
            raise forms.ValidationError("文章标签长度需要大于6")
        elif len(label) > 20:
            raise forms.ValidationError("文章标签长度需要小于20")
        else:
            return label
