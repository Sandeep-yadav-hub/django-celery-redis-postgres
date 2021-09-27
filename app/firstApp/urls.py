from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('tasks/<task_id>/', views.get_status, name='getstatus'),
    path('add/', views.run_task, name='add'),
]