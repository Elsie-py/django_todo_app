from django.urls import path, include
from .import views

urlpatterns = [

    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('api/', include('todo_app.api.urls')),
]
