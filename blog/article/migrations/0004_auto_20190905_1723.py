# Generated by Django 2.0.7 on 2019-09-05 09:23

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_examplemodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='content',
            field=mdeditor.fields.MDTextField(default='ok,现在开始编写你的内容吧！'),
        ),
    ]
