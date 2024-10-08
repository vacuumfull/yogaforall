# Generated by Django 5.0 on 2024-07-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя'),
        ),
    ]
