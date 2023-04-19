# Generated by Django 3.2 on 2023-04-19 11:44

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20230419_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(on_delete=models.SET(reviews.models.get_deleted_category), related_name='titles', to='reviews.category', verbose_name='Категория'),
        ),
    ]