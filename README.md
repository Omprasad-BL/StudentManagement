# djnago based full stack project to learn flow of djnago framework

# mcaprojs

steps invovled to get started with django
step 1 create a project folder
step 2 inside that folder "pip install virtualenv"
step 3 assign private virtual machine to folder "python -n venv venv "
step 4 activate bat configure file " venv/Scripts/activate.bat
<!-- if not wokring add some configuration paths -->
<!-- Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope  Process -->
<!-- venv/Scripts/activate  -->
step 5 install django "pip install django" 
step 6 create django project "djnago-admin startproject projectname ." NOTE: here dot helps to create PROJECTC  in current directory ONLY FOR PROJECTS MAIN APP WHICH HANDLES ALL smaller DJANGO APPS

step 7 create then create other apps for MAIN_APP app like above "django-admin startapp appName"    ONLY FOR APPS (djnago Modules) SMALL APPS WHICH WHICH ARE handled by  DJANGO Project

step 8 after all project set-up use "python manage.py runserver" to run or start project 
Project Flow-->manage.py-->mainApp "which created with dot above" --> other apps
step 9 to create djnago-admin use "python manage.py createsuperuser"
       or "python manage.py createsuperuser --username admin --email admin@example.com"

step 10 each time you deal with python sqlite versions follow steps
        step A: python manage.py makemigrations
        step B: python manage.py migrate 
        NOTE: migrate will help to synch data class/ plain class each time they changed by user

step 11 restart once migration happens to let know machine Objects properties changed 

WARNING : never use "python manage.py startapp main"  MORE THAN ONCE
