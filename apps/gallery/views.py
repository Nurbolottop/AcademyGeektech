from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settins,Mailing
from apps.gallery.models import Gallery

# Create your views here.

def gallery(request):
    settings = Settins.objects.latest('id') 
    gallery = Gallery.objects.all()
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
        'gallery': gallery,



    }

    return render(request, 'gallery.html', context)