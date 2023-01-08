from django.shortcuts import render
from apps.settings.models import Settins
# Create your views here.

def course(request):
    settings = Settins.objects.latest('id') 



    context = {
        'settings': settings,


    }

    return render(request, 'course.html', context)