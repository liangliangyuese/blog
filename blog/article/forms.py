# coding=utf-8
from django import forms
from .models import Article, ArticleState


class ArticleForm(forms.Form):
    title = forms.CharField(label="article title", max_length=20)
    label = forms.CharField(label="article label", max_length=20)
    content = forms.CharField(label="article content")

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
