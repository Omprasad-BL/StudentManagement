from django.contrib import admin

# Register your models here.
from .models import Course,Student,Assignment,StudentProfile
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(StudentProfile)