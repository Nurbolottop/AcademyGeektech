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
