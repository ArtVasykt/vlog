# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160403_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='C:\\Users\\Администратор\\PycharmProjects\\vlog\\media\\default.jpg', upload_to='avatars/%d/%m/%Y', verbose_name='аватар'),
        ),
    ]