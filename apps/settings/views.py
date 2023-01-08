from django.shortcuts import render
from apps.settings.models import Settins,Slides,It
from apps.contacts.models import Contacts

# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slide = Slides.objects.latest('id') 
    it = It.objects.all() 
    contacts = Contacts.objects.latest('id') 

    context = {
        'settings': settings,
        'slide': slide,
        'it': it,
        'contacts': contacts,


    }

    return render(request, 'index.html', context)