from django.shortcuts import render,redirect

from apps.settings.models import Settins
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
    if request.method == "POST":
        if 'comment' in request.POST:
                message = request.POST.get('message')
                
                comment = Comment.objects.create(name = request.name, email = news, message = message)
                return redirect('news_detail', news.id)
    context = {
        'settings': settings,
        'news': news,
        'contacts': contacts,
        'random_new': random_new,

    }
    return render(request, 'blog-details.html', context)