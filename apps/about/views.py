from django.shortcuts import render
from apps.settings.models import Settins,Number
from apps.contacts.models import Contacts
from apps.about.models import About

# Create your views here.

def about(request):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    number = Number.objects.latest('id') 
    about  = About.objects.latest('id')
    context = {
        'settings': settings,
        'contacts': contacts,
        'number': number,
        'about': about,


    }

    return render(request, 'about.html', context)