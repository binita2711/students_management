from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# User Model with role (Admin or Staff)
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

    # Avoid conflicts with Django's built-in User model
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Admission Model
class Admission(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    date_of_admission = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])

# Marks Model
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    total_marks = models.IntegerField()
