# coding=utf-8
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path('article/', include('article.urls')),
    path('user/', include('user.urls')),
    path('favicon.ico', serve, {'path': 'static/image/favicon.ico'}),
    # 配置静态文件路由
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),

]
# 定义错误跳转页面
handler403 = views.page_permission_denied
handler404 = views.page_ont_found
handler500 = views.page_error
