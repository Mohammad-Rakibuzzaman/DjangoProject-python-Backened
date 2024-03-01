from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('add/', views.add_p, name="add_p"),
     path('delete/<int:roll>', views.delete_p, name="delete_p"),
]