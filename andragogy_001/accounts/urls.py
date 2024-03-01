from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    # path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    # path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),

    path('profile/edit/pass_change/', views.pass_change, name='pass_change'),

    path('add_userdetails/', views.add_userdetails, name="add_userdetails"),

    path('edit/userdetails/<int:id>', views.edit_userdetails, name='edit_userdetails'),
    path('delete/<int:id>', views.delete_userdetails, name="delete_userdetails"),
]