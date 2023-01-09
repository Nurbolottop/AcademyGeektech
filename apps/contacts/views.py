from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.settings.models import Settins,Mailing
from apps.contacts.models import Contacts,Contact_detail
# Create your views here.

def contact(request):
    settings = Settins.objects.latest('id') 
    contacts = Contacts.objects.latest('id') 
    if request.method =="POST":
        email = request.POST.get('email')
        Mailing.objects.create(email = email)

        send_mail(
            f'{email}',

            f'Здравствуйте {email}, Спасибо за то что подписались на нашу рассылку,',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name,email = email,message = message,phone = phone)
        send_mail(
            f'{message}',

            f'Здравствуйте {name}, Спасибо за отклик, мы скоро с вами свяжемся.Ваше сообщение: {message} Ваша почта: {email}. Ваш номер: {phone}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
    context = {
        'settings': settings,
        'contacts': contacts,
    }
    return render(request, 'contact.html', context)