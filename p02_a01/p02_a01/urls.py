
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first/', include('first_app.urls')),
    path('card/', include('card_app.urls')),
    path('', views.base),
    
]
