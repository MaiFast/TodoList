from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('reset-tasks/', views.reset_tasks, name='reset_tasks'),

]
