"""geektech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.about.views import about,team_detail
from apps.settings.views import index
from apps.contacts.views import contact
from apps.course.views import course,course_details
from apps.gallery.views import gallery
from apps.news.views import news, news_details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('course/', course, name="course"),
    path('course_detail/', course_details, name="course_detail"),
    path('gallery/', gallery, name="gallery"),
    path('news/', news, name="news"),
    path('news_details/', news_details, name="news_detail"),
    path('about/', about, name="about"),
    path('team_detail/', team_detail, name="team_detail"),

]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)