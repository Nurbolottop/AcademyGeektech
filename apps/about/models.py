from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=255,verbose_name="О нас")
    image = models.ImageField(upload_to="about_image/", verbose_name="Фотография")
    descriptions = models.TextField(verbose_name="Описание")

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural ="О нас"

class Teams(models.Model):
    image = models.ImageField(
        upload_to="techer_image/",
        verbose_name="Фотография учителя"
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Имя учителя"
    )
    work = models.CharField(
        max_length=255,
        verbose_name="Должность учителя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
        )

    email = models.CharField(
        max_length=255,
        verbose_name="Почта учителя"
        )
    faceebook = models.URLField(
        verbose_name="Facebook",
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True, null=True
    )
    telegram = models.URLField(
        verbose_name="Telegram",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="WhatsApp",
        blank=True, null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"