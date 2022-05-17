from django.urls import path
from courseapp import views

urlpatterns = [
    path('', views.CourseApi.as_view(), name='courses'),
    path('<int:id>', views.CourseApi.as_view(), name='course'),
]