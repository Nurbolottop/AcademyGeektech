from django.shortcuts import render
from apps.settings.models import Settins,Number
from apps.contacts.models import Contacts
from apps.about.models import About,Teams

# Create your views here.

def about(request):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    number = Number.objects.latest('id') 
    about  = About.objects.latest('id')
    team  = Teams.objects.all()
    context = {
        'settings': settings,
        'contacts': contacts,
        'number': number,
        'about': about,
        'team': team,
    }

    return render(request, 'about.html', context)

def team_detail(request,id):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    number = Number.objects.latest('id') 
    about  = About.objects.latest('id') 
    team  = Teams.objects.get(id = id)
    context = {
        'settings': settings,
        'contacts': contacts,
        'number': number,
        'about': about,
        'team': team,
    }

    return render(request, 'team-details.html', context)