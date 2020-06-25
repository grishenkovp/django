from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TasksListView, TaskDetailView, TaskCreateView

app_name = 'task'

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('status/<slug:status>/', views.tasks_filter, name='tasks_filter'),
    path('<int:id>/<slug:slug>/', TaskDetailView.as_view(), name='task'),
    path('create_task/new/', TaskCreateView.as_view(), name='new_task'),
]
# path('', views.tasks, name='tasks'),
# path('<int:id>/<slug:slug>/', views.task, name='task'),
# path('create_task/', views.create_task, name='new_task'),