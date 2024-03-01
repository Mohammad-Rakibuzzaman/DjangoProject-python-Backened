from django.urls import path, include
from . import views

urlpatterns = [
    path('about_uss/', views.about_us, name= 'about_uss'),
]
