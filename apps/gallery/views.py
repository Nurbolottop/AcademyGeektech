from django.shortcuts import render
from apps.settings.models import Settins
from apps.gallery.models import Gallery

# Create your views here.

def gallery(request):
    settings = Settins.objects.latest('id') 
    gallery = Gallery.objects.all()


    context = {
        'settings': settings,
        'gallery': gallery,



    }

    return render(request, 'gallery.html', context)