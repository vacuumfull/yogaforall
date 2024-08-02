import os
from django.db import models
from uuid import uuid4

def file_path(_instance, filename):
	"""Path and name to image file."""
	file_path = os.path.join('dist/files', str(uuid4()))
	ext = filename.split('.')[-1]
	return '{}.{}'.format(file_path, ext)

class Appeal(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    email = models.EmailField(max_length=254, verbose_name="Email", null=True, blank=True)
    phone = models.CharField(max_length=64, verbose_name="Номер телефона")
    content = models.TextField(verbose_name="Сообщение", null=True, blank=True)
    is_checked = models.BooleanField(default=False, verbose_name="Обработана ли")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', 'is_checked']
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return "{}: {}".format(self.name, self.email)

