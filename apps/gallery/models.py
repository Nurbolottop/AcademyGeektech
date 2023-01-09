from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(
        upload_to="gallery_image/",
        verbose_name="Фотография"
    )


    
    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"

class Contact_detail(models.Model):
    name =models.CharField(max_length =255,verbose_name="Имя")
    phone =models.CharField(max_length =255,verbose_name="Номер")

    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Сообщение")


    def __str__(self):
        return f"{self.name} {self.message}"

    class Meta:
        verbose_name_plural = "Полученные сообщения "
        verbose_name = "Полученные сообщения "  