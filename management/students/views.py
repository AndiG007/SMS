from django.shortcuts import render
from .models import Student

def hello_world(request):
    value = Student.objects.all()
    context = {
        'student': value
    }
    return render(request, 'students/index.html', context)
