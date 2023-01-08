from django.db import models

# # Create your models here.
class Course(models.Model):
    image = models.ImageField(
        upload_to="couse_image",
        verbose_name="Фотография"
    )
    name = models.CharField(
        max_length=244,
        verbose_name="Название курса"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"
