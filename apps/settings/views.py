from django.shortcuts import render
from apps.settings.models import Settins,Slides,It
# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slide = Slides.objects.latest('id') 
    it = It.objects.all() 


    context = {
        'settings': settings,
        'slide': slide,
        'it': it,

    }

    return render(request, 'index.html', context)