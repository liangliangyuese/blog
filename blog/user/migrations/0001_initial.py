# Generated by Django 2.0.7 on 2019-07-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='自增id')),
                ('nick_name', models.CharField(max_length=30, unique=True, verbose_name='用户昵称')),
                ('phone', models.IntegerField(max_length=11, unique=True, verbose_name='手机号')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
            ],
        ),
    ]
