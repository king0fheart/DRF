from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name