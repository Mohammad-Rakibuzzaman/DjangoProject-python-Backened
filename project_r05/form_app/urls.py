from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('about/', views.about_us, name= 'about_us'),
    path('form/', views.submit_form, name= 'submit_form'),
    # path('django_form/', views.DjangoForm, name= 'django_form'),
    # path('django_form/', views.StudentForm, name= 'django_form'),
    path('django_form/', views.PasswordValidation, name= 'django_form'),
]