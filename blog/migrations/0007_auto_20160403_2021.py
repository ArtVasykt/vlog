# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160403_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='avatars/%d/%m/%Y', verbose_name='аватар'),
        ),
    ]