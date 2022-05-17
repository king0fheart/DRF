from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length=40)
    address = models.CharField(max_length=80)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name}"