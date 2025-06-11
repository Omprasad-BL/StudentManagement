from django.urls import path
from . import views
urlpatterns =[
    path("",views.home, name="home"),
    path("login/",views.StudentLogin, name="login"),
    path("dashboard/",views.StudentDashBoard, name="dash"),
    path("create/",views.CreateStudent,name="Student"),
    path("create_course/",views.CreateCourse,name="Course")
    #http://127.0.0.1:8000/student/ 
    #https://github.com/Abhishek-BG/mcaprojs
]