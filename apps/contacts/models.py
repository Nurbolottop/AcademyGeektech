from django.db import models

# Create your models here.
class Contacts(models.Model):
    address = models.CharField(
        max_length = 255,
        verbose_name="Адрес: "
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Тел.ном: "
    )
    email = models.CharField(
        max_length=255,
        verbose_name="Почта: "
    )
    faceebook = models.URLField(
        verbose_name="Facebook",
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="YouTube",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="WhatsApp",
        blank=True, null=True
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"