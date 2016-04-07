import os

from django.db import models
from django.utils import timezone

from vlog.settings import MEDIA_URL


class Profile(models.Model):
    name = models.CharField(max_length=60, verbose_name='имя')
    password = models.CharField(max_length=60, verbose_name='пароль')
    date_of_registration = models.DateField(verbose_name='дата регистрации', default=timezone.now)
    description = models.TextField(verbose_name='о себе', max_length=10000, null=True, blank=True)
    avatar = models.ImageField(verbose_name='аватар', upload_to='avatars/%Y/%m/%d', default='avatars/default.jpg')

    def relative_avatar_url(self):
        return os.path.join(MEDIA_URL, self.avatar.url)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    description = models.TextField(verbose_name='подробно')
    pub_date = models.DateTimeField(verbose_name='дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
