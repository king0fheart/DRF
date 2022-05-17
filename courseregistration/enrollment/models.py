from django.db import models
from courseapp.models import Course
from studentapp.models import Student 

# Create your models here.
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
    # course = models.ManyToManyField(Course, db_column='courseId')
    # student = models.ManyToManyField(Student, db_column='studentId')
    grade = models.CharField(blank=True, max_length=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)