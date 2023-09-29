from django.contrib import admin
from django.urls import path
from .views import gamesapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games-api/', gamesapi),
]
