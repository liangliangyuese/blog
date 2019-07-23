# Generated by Django 2.0.7 on 2019-07-16 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('label', models.CharField(max_length=20, verbose_name='文章标签')),
                ('collect', models.IntegerField(verbose_name='文章收藏数量')),
                ('like', models.IntegerField(verbose_name='文章点赞数量')),
                ('title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章正文')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('like_state', models.BooleanField(verbose_name='喜欢的状态')),
                ('collect_state', models.BooleanField(verbose_name='收藏的状态')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='目标文章id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='操作用户的id')),
            ],
        ),
    ]