from django.shortcuts import render
from apps.settings.models import Settins,Slides,It,Number
from apps.contacts.models import Contacts
from apps.course.models import Course
from apps.news.models import News
from apps.about.models import About

# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slide = Slides.objects.latest('id') 
    it = It.objects.all() 
    contacts = Contacts.objects.latest('id') 
    course = Course.objects.all()
    news = News.objects.all()
    number = Number.objects.latest('id')
    about = About.objects.latest('id')


    context = {
        'settings': settings,
        'slide': slide,
        'it': it,
        'contacts': contacts,
        'course': course,
        'news': news,
        'number': number,
        'about': about,

    }

    return render(request, 'index.html', context)