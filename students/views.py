from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('student_dashboard')
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

def StudentDashboard(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',context={'peoples':students})
                                                # here its context data
def student_list(request):
    students = Student.objects.all()
    # return HttpResponse(students)
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request,pk):
    student = get_object_or_404(Student, pk=pk)
    # return HttpResponse("<h1> Hello world </h1>")
    return render(request, 'students/student_detail.html', {'student': student})


def student_update(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = StudentForm(instance=student) #get
    return render(request, 'students/student_form.html',
                   {'form': form})


def student_delete(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_dashboard')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
