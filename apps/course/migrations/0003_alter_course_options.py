# Generated by Django 4.1.5 on 2023-01-08 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курсы', 'verbose_name_plural': 'Курсы'},
        ),
    ]
