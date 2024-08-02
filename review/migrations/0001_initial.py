# Generated by Django 5.0 on 2024-07-28 11:30

import review.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=review.models.file_path, verbose_name='Изображение')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
                'ordering': ['-created_at', 'published'],
            },
        ),
    ]
