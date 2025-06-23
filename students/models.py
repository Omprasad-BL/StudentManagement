from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateTimeField()
    def __str__(self):
        return f"{self.title} - {self.course.name}"




class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    joined_on = models.DateTimeField(auto_now_add=True)
    enrolled_courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.name}: Verified:{self.is_verified}"
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)  # OneToOneField
    address = models.TextField()
    phone = models.CharField(max_length=15)
    profile_picture_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Profile of {self.student.name}"
    
# class StudentProfile(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
#     address = models.TextField(null=True, blank=True)
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     profile_picture_url = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return f"Profile of {self.student.name}"
