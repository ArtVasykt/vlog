# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_registration',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата регистрации'),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='о себе'),
        ),
    ]
