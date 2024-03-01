from django.contrib import admin
from django.urls import path
from . import views
from .views import DetailTutionView
urlpatterns = [
    # path('add/', views.add_post, name='add_post'),
    path('add/', views.AddTutionCreateView.as_view(), name='add_tution'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('edit/<int:id>/', views.EditTutionView.as_view(), name='edit_tution'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('delete/<int:id>/', views.DeleteTutionView.as_view(), name='delete_tution'),
    # path('details/<int:id>/', views.DetailTutionView.as_view(), name='detail_tution'),

    path('details/<int:pk>/', views.DetailTutionView.as_view(), name='tution_details'),
    path('details/<int:pk>/', views.DetailTutionView2.as_view(), name='tution_details2'),
   
    path('apply/<int:id>/', views.ApplyForTutionView.as_view(), name='apply_for_tution'),
]