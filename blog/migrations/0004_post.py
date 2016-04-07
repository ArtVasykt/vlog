# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile_referral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='подробно')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name_plural': 'посты',
                'verbose_name': 'пост',
            },
        ),
    ]
