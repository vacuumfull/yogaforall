# Generated by Django 5.0 on 2024-07-29 13:01

import review.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=review.models.file_path, verbose_name='Изображение'),
        ),
    ]
