# Generated by Django 4.1.5 on 2023-01-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_slides_description_slide1_slides_name_slide1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slides',
            name='description_slide',
        ),
        migrations.RemoveField(
            model_name='slides',
            name='name_slide',
        ),
        migrations.RemoveField(
            model_name='slides',
            name='slide_image',
        ),
        migrations.AddField(
            model_name='slides',
            name='description_slide2',
            field=models.TextField(default=1, verbose_name='Описание второго слайда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='name_slide2',
            field=models.TextField(default=1, verbose_name='Название  второго слайда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='slide_image2',
            field=models.ImageField(default=1, upload_to='slide_image', verbose_name='Фотография второго слайда'),
            preserve_default=False,
        ),
    ]
