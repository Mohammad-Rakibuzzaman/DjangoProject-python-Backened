from django.urls import path
from . import views
from .views import home,ArticleDetailView, AddPostView, UpdatePostView
urlpatterns = [
    path('', home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('privacy', views.privacy, name="privacy"),
    path('laptop', views.laptop , name="laptop"),
    path('document', views.document , name="document"),
    
]
