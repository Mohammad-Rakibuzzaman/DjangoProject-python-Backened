from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
]