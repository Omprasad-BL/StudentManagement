from django.urls import path
from . import views
urlpatterns =[
    # student routings
    # path("",views.home, name="home"),
    path("home/",views.home, name="home"),
    path("login/",views.StudentLogin , name="login"),
    path("student_dashboard/", views.StudentDashboard, name="student_dashboard"),
    path("student/student_create/",views.CreateStudent,name="student_create"),
    path("student/<int:pk>/student_detail",views.student_detail,name="student_detail"),
    path("student/<int:pk>/student_update/",views.student_update,name="student_update"),    
    path("student/<int:pk>/delete/",views.student_delete,name="student_delete"),

    #  course routings
    path("create_course/",views.CreateCourse,name="Course")




    #http://127.0.0.1:8000/student/ 
    #https://github.com/Abhishek-BG/mcaprojs
]