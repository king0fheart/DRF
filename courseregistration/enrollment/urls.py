from django.urls import path
from enrollment import views

urlpatterns = [
    path('', views.EnrollmentApi.as_view(), name='enrollments'),
    path('<int:id>', views.EnrollmentApi.as_view(), name='enrolled-id'),
    path('course', views.EnrolledStudentApi.as_view(), name='enrolled-all-student-in-course'),
    path('course/<int:enroll_id>', views.EnrolledStudentApi.as_view(), name='enrolled-student-in-course'),

    path('student', views.EnrolledCourseApi.as_view(), name='list-of-all-enrolled-students'),
    path('student/<int:std_id>', views.EnrolledCourseApi.as_view(), name='list-of-enrolled-coures-of-student'),
]