from django.shortcuts import render
from apps.settings.models import Settins
from apps.contacts.models import Contacts
# Create your views here.

def contact(request):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    context = {
        'settings': settings,
        'contacts': contacts,
    }
    return render(request, 'contact.html', context)