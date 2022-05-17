from django.urls import path
from api import views

urlpatterns = [
    path('', views.TaskApi.as_view(), name='tasks'),
    path('task/<int:id>', views.TaskApi.as_view(), name='task'),
]