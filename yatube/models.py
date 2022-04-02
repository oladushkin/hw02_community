from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Название недолжно привышать 200 символов.'
    )
    slug = models.SlugField(
        max_length=20,
        unique=True,
        blank=False,
        verbose_name='Slug вашей группы',
        help_text='Пишите на английском языке'
    )
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст сообщения')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='group'
    )

    class Meta:
        ordering = ('-pub_date')
