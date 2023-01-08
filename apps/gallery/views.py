from django.shortcuts import render
from apps.settings.models import Settins
# Create your views here.

def gallery(request):
    settings = Settins.objects.latest('id') 



    context = {
        'settings': settings,


    }

    return render(request, 'gallery.html', context)