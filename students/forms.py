# create 
from django import forms
from .models import Student,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model =Student
        fields= '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        fields= '__all__'