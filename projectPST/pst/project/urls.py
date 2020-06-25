from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView

app_name = 'project'

urlpatterns = [path('', ProjectsListView.as_view(), name='projects'),
               path('status/<slug:status>/', views.projects_filter, name='projects_filter'),
               path('<slug:slug>/', ProjectDetailView.as_view(), name='project'),
               path('create_project/new/', ProjectCreateView.as_view(), name='new_project'),]



# path('', views.projects, name='projects'),
# path('<slug:slug>/', views.project, name='project'),
 # path('create_project/', views.create_project, name='new_project'),

