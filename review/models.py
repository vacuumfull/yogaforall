import os
from django.db import models
from uuid import uuid4


def file_path(_instance, filename):
	"""Path and name to image file."""
	file_path = os.path.join('reviews', str(uuid4()))
	ext = filename.split('.')[-1]
	return '{}.{}'.format(file_path, ext)


class Review(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name="Имя")
    content = models.TextField(null=True, blank=True, verbose_name="Содержание")
    date = models.DateField(null=True, blank=True, verbose_name="Дата отзыва")
    image = models.ImageField(upload_to=file_path, null=True, blank=True, verbose_name="Изображение")
    published = models.BooleanField(default=False, verbose_name="Опубликовать")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'published']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'