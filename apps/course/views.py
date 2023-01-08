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
    
def course_detils(request):
    settings = Settins.objects.latest('id') 
    course = Course.get(id =id)
    context = {
        'settings': settings,
        'course': course,
    }
    return render(request, 'course_detils.html', context)
