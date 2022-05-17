from django.urls import path
from studentapp import views

urlpatterns = [
    path('', views.StudentApi.as_view(), name='students'),
    path('<int:id>', views.StudentApi.as_view(), name='student'),
]