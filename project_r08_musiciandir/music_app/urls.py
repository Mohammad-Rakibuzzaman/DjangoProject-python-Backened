from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('add_music/', views.add_music, name="add_music"),
    path('add_album/', views.add_album, name="add_album"),
    path('edit/album/<int:id>', views.edit_post, name='edit_post'),
    path('edit/musician/<int:id>', views.edit_musician, name='edit_musician'),
    path('delete/<int:id>', views.delete_music, name="delete_music"),
]