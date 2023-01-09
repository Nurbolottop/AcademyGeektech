from django.db import models

# # Create your models here.
class News(models.Model):
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
        verbose_name = "Новости"
        verbose_name_plural = "Новости"



class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name="post_comment")

    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.CharField(max_length=255, verbose_name="Почта")
    message = models.CharField(max_length=255,verbose_name="Сообщение")
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name

    class Meta:
        # on_delete=models.CASCADE,
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"
