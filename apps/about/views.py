from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settins,Number,Mailing
from apps.contacts.models import Contacts
from apps.about.models import About,Teams

# Create your views here.

def about(request):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    number = Number.objects.latest('id') 
    about  = About.objects.latest('id')
    team  = Teams.objects.all()
    if request.method =="POST":
        email = request.POST.get('email')
        Mailing.objects.create(email = email)

        send_mail(
            f'{email}',

            f'Здравствуйте {email}, Спасибо за то что подписались на нашу рассылку,',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
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