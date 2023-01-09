from django.shortcuts import render,redirect
from django.core.mail import send_mail

from apps.settings.models import Settins,Slides,It,Number,Mailing
from apps.contacts.models import Contacts
from apps.course.models import Course
from apps.news.models import News
from apps.about.models import About

# Create your views here.

def index(request):
    settings = Settins.objects.latest('id') 
    slide = Slides.objects.latest('id') 
    it = It.objects.all() 
    contacts = Contacts.objects.latest('id') 
    course = Course.objects.all()
    news = News.objects.all()
    number = Number.objects.latest('id')
    about = About.objects.latest('id')
    if request.method =="POST":
        email = request.POST.get('email')
        Mailing.objects.create(email = email)

        send_mail(

            f'Здравствуйте {email}, Спасибо за то что подписались на нашу рассылку,',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')



    context = {
        'settings': settings,
        'slide': slide,
        'it': it,
        'contacts': contacts,
        'course': course,
        'news': news,
        'number': number,
        'about': about,

    }

    return render(request, 'index.html', context)