from django.shortcuts import render,redirect
from django.core.mail import send_mail
from apps.settings.models import Settins,Mailing
from apps.news.models import News,Comment
from apps.contacts.models import Contacts
# Create your views here.

def news(request):
    settings = Settins.objects.latest('id') 
    news = News.objects.all()
    contacts = Contacts.objects.latest('id') 

    context = {
        'settings': settings,
        'news': news,
        'contacts': contacts,

    }
    return render(request, 'blog.html', context)

def news_details(request,id):
    random_new = News.objects.all().order_by('?')

    settings = Settins.objects.latest('id') 
    news = News.objects.get(id =id)
    contacts = Contacts.objects.latest('id') 
    # if request.method =="POST":
    #     email = request.POST.get('email')
    #     Mailing.objects.create(email = email)

    #     send_mail(
    #         f'{email}',

    #         f'Здравствуйте {email}, Спасибо за то что подписались на нашу рассылку,',
    #         "noreply@somehost.local",
    #         [email])
        
    #     return redirect('index')

    if request.method == "POST":
        if 'comment' in request.POST:
                name = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')
                created = request.POST.get('created')
                comment = Comment.objects.create(name = name, post = news, email = email, message = message,created = created)
                return redirect('news_detail', news.id)
    context = {
        'settings': settings,
        'news': news,
        'contacts': contacts,
        'random_new': random_new,

    }
    return render(request, 'blog-details.html', context)