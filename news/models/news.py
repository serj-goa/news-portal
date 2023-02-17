from django.db import models
from django.urls import reverse

from .category import Category


class News(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Заголовок')
    content = models.TextField(max_length=1024, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    views = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})
