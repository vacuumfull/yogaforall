import os
from uuid import uuid4
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from uuslug import uuslug


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, verbose_name="Алиас")
    content = models.TextField(verbose_name="Содержание")
    published = models.BooleanField(default=False, verbose_name="Опубликовать")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to=image_path, null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.published)

    class Meta:
        ordering = ['name', 'published']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


@receiver(pre_save, sender=Product)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    if instance.pk is None:
        instance.slug = uuslug(instance.name, instance=instance)