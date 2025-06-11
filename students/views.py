from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Student
from .forms import StudentForm,CourseForm

pages=[{"name":"Home page" ,"url":"home" },
        {"name":"Login Page","url":"login"}]


people=[
     {"name":"OMprasad","age":25,"email":"om@gmail.com","active":True},
     {"name":"adarsh","age":37,"email":"adi@gmail.com","active":True},
     {"name":"nandu","age":47,"email":"nandu@gmail.com","active":False},
     {"name":"Dhanush","age":50,"email":"dhanu@gmail.com","active":False}
    ]


# student create
def CreateStudent(req):
    if(req.method=='POST'):
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm()
    return  render(req,'students/student_create.html',{'form':form})

def CreateCourse(req):
    if(req.method=='POST'):
        form= CourseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CourseForm()
    return render(req,'students/create_course.html',{'form':form})


def home(request): #controller 
    students = Student.objects.all()
    # context={
    #     'students':people
    # }
       
    # return HttpResponse("<h1>Welcome to Students Home Page</h1>")
    return render(request,'students/home.html',context={'items':pages,'peoples':students})
                                                # here its context data

def StudentLogin(request):
    # return HttpResponse(" <h1>Login Page</h1>")
    return render(request,'students/login.html',context={'items':pages,'peoples':people})

def StudentDashBoard(request):
    return HttpResponse(" <h1>Your Profile</h1>")