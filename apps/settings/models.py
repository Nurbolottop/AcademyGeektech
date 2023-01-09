from django.db import models

# Create your models here.
class Settins(models.Model):

    image = models.ImageField(
        upload_to='Site_image',
        verbose_name="Логотип"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

class Slides(models.Model):
    slide_image1 = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография первого  слайда"
    )
    name_slide1 = models.TextField(
        verbose_name="Название  первого  слайда"
    )
    description_slide1 = models.TextField(
        verbose_name="Описание  первого слайда"
    )
    slide_image2 = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография второго слайда"
    )
    name_slide2 = models.TextField(
        verbose_name="Название  второго слайда"
    )
    description_slide2 = models.TextField(
        verbose_name="Описание второго слайда"
    )
    def __str__(self):
        return self.name_slide1

    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайды"

class It(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание!"
    )
    image = models.ImageField(
        upload_to="it",
        verbose_name="Фотография"
        )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ПОЧЕМУ IT - ЭТО КРУТО?"
        verbose_name_plural = "ПОЧЕМУ IT - ЭТО КРУТО?"

class Number(models.Model):
    teacher = models.CharField(
        max_length=255,
        verbose_name="Учителя"
    )
    students = models.CharField(
        max_length=255,
        verbose_name="Ученики"
    )
    course = models.CharField(
        max_length=255,
        verbose_name="Курсы"
    )
    office = models.CharField(
        max_length=255,
        verbose_name="Офисы"
    )

    def __str__(self):
        return self.teacher

    class Meta:
        verbose_name = "Geektech в цифрах"
        verbose_name_plural = "Geektech в цифрах"

