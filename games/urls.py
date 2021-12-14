"""URL patterns for this app 'games'."""

from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    # Home page/Index
    path('', views.index, name='index'),
    # Games-page
    path('titles/', views.titles, name='titles'),
    # Descriptions and other details per game-entry
    path('titles/<int:title_id>/', views.title, name='title'),
]