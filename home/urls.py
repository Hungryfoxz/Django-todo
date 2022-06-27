from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('show/<int:pk>/', views.show, name='show'),
]
