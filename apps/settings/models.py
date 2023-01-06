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
    slide_image = models.ImageField(
        upload_to="slide_image",
        verbose_name="Фотография слайда"
    )
    name_slide = models.TextField(
        verbose_name="Название  слайда"
    )
    description_slide = models.TextField(
        verbose_name="Описание слайда"
    )
    def __str__(self):
        return self.name_slide

    class Meta:
        verbose_name = "Слайды"
        verbose_name_plural = "Слайды"