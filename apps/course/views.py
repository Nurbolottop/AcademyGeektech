from django.shortcuts import render
from apps.settings.models import Settins
from apps.course.models import Course
from apps.contacts.models import Contacts

# Create your views here.

def course(request):
    settings = Settins.objects.latest('id') 
    course = Course.objects.all()
    contacts = Contacts.objects.latest('id') 

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

    context = {
        'settings': settings,
        'course': course,
        'contacts': contacts,

    }
    return render(request, 'courses_details.html', context)
