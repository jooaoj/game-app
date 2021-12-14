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
    # Page for adding a new title
    path('new_title/', views.new_title, name='new_title'),
    #Page for adding new enteries.
    path('new_entry/<int:title_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]