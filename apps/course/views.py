from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settins,Mailing
from apps.course.models import Course
from apps.contacts.models import Contacts

# Create your views here.

def course(request):
    settings = Settins.objects.latest('id') 
    course = Course.objects.all()
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

    context = {
        'settings': settings,
        'course': course,
        'contacts': contacts,

    }
    return render(request, 'course.html', context)

def course_details(request,id):

    settings = Settins.objects.latest('id') 
    course = Course.objects.get(id =id)
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

    context = {
        'settings': settings,
        'course': course,
        'contacts': contacts,

    }
    return render(request, 'courses_details.html', context)
