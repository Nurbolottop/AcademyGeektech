from django.shortcuts import render
from apps.settings.models import Settins
# Create your views here.

def contact(request):
    settings = Settins.objects.latest('id') 



    context = {
        'settings': settings,


    }

    return render(request, 'contact.html', context)