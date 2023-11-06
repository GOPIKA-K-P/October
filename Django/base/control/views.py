from django.shortcuts import render
from .models import Student

# Create your views here.
def control(request):
    students=Student.objects.all()
    return render(request,'basic.html',{'students':students})

