from django.contrib import admin
from django.urls import path
from Evaluation import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contactos/', views.contacts, name='Home'),
]