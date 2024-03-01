from django.urls import path, include
from . import views

urlpatterns = [
    path('show_itemss/', views.show_items, name= 'show_itemss'),
]
