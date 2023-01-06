from django.shortcuts import render
from apps.settings.models import Settins,Slides
# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slides = Slides.objects.latest('id') 

    context = {
        'settings': settings,
        'slides': slides,
    }

    return render(request, 'index.html', context)