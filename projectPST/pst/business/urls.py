from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'business'

urlpatterns = [
    path('create_city/', views.create_city, name='new_city'),
    path('create_client/', views.create_client, name='new_client'),

]
