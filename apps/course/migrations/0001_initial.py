# Generated by Django 4.1.5 on 2023-01-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='couse_image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=244, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ('id',),
            },
        ),
    ]
