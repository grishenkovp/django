from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import StepsListView, StepDetailView, StepCreateView

app_name = 'step'

urlpatterns = [

    path('', StepsListView.as_view(), name='steps'),
    path('status/<slug:status>/', views.steps_filter, name='steps_filter'),
    path('<int:id>/<slug:slug>/', StepDetailView.as_view(), name='step'),
    path('create_step/new/', StepCreateView.as_view(), name='new_step'),
]
# path('', views.steps, name='steps'),
# path('<int:id>/<slug:slug>/', views.step, name='step'),
# path('create_step/', views.create_step, name='new_step'),