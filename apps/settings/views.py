from django.shortcuts import render
from apps.settings.models import Settins,Slides,It
from apps.contacts.models import Contacts
from apps.course.models import Course


# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slide = Slides.objects.latest('id') 
    it = It.objects.all() 
    contacts = Contacts.objects.latest('id') 
    course = Course.objects.all()

    context = {
        'settings': settings,
        'slide': slide,
        'it': it,
        'contacts': contacts,
        'course': course,
    }

    return render(request, 'index.html', context)