from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Student
def home(request): #controller 
    students = Student.objects.all()
    # return HttpResponse("<h1>Welcome to Students Home Page</h1>")
    return render(request,'students/home.html',{'students':students})

def StudentLogin(request):
    # return HttpResponse(" <h1>Login Page</h1>")
    return render(request,'students/login.html')

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")