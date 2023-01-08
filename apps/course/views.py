from django.shortcuts import render
from apps.settings.models import Settins
from apps.course.models import Course

# Create your views here.

def course(request):
    settings = Settins.objects.latest('id') 
    course = Course.objects.all()
    context = {
        'settings': settings,
        'course': course,
    }
    return render(request, 'course.html', context)

def course_details(request,id):

    settings = Settins.objects.latest('id') 
    course = Course.objects.get(id =id)

    context = {
        'settings': settings,
        'course': course,
    }
    return render(request, 'courses_details.html', context)
