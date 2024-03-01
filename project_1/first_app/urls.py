from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses),
    path('', views.home),
    path('about/', views.about),
 
]
