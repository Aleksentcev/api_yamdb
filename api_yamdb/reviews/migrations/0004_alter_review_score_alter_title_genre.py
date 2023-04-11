# Generated by Django 4.2 on 2023-04-11 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_category_slug_genre_slug_alter_category_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], max_length=5, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ForeignKey(default=1, help_text='Жанр произведения', on_delete=django.db.models.deletion.CASCADE, to='reviews.genre', verbose_name='Жанр'),
            preserve_default=False,
        ),
    ]