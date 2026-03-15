from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks'),
    path('create/', views.create_task, name='task-create'),
    path('delete/<int:pk>/', views.delete_task, name='task-delete'),
    path('toggle/<int:pk>/', views.toggle_task, name='task-toggle'),
]