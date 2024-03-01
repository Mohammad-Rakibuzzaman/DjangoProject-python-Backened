from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.Table, name="table"),
    path('', views.Table, name="Table"),
    path('create', views.categorycreate, name="categorycreate"),
    path('inserted', views.categoryaddprocess, name="categoryaddprocess"),
    path('delete/<int:date>', views.categorydelete, name="categorydelete"),
    # path('edit/<int:id>', views.categoryedit, name="categoryedit"),
    # path('update/', views.categoryupdate, name="categoryupdate"),
]