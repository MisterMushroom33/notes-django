from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('add/', views.add_note, name='add_note'),
    path('theme/<str:theme_name>/', views.set_theme, name='set_theme'),
]