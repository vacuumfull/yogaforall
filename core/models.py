import os
from django.db import models
from uuid import uuid4


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Meta(models.Model):
    title = models.CharField(max_length=128, verbose_name="Мета title")
    description = models.CharField(max_length=256, verbose_name="Мета description")
    intro_text = models.CharField(max_length=256, verbose_name="Печатающийся текст")

    class Meta:
        verbose_name = "Мета информация"
        verbose_name_plural = "Мета информация"


class About(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название раздела")
    left_content = models.TextField(verbose_name="Контент слева")
    right_content = models.TextField(verbose_name="Контент справа")

    class Meta:
        verbose_name = "Раздел обо мне"
        verbose_name_plural = "Раздел обо мне"


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, verbose_name="Раздел")
    image = models.ImageField(upload_to=image_path, verbose_name="Изображение")
    name = models.CharField(max_length=128, null=True, blank=True, verbose_name="Название")

    class Meta:
        verbose_name = "Изображения раздела обо мне"
        verbose_name_plural = "Изображения раздела обо мне"


class SectionName(models.Model):
    product_name = models.CharField(max_length=64, verbose_name="Название раздела продуктов")
    review_name = models.CharField(max_length=64, verbose_name="Название раздела отзывов")

    class Meta:
        verbose_name = "Название раздела"
        verbose_name_plural = "Названия разделов"