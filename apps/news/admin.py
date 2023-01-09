from django.contrib import admin
from apps.news.models import News, Comment
# Register your models here.
admin.site.register(News)
admin.site.register(Comment)
