from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_page, name='dashboard'),
    path('create/', views.create_shoe, name='create_shoe'),
    path('<int:pk>/view_shoe', views.view_shoe, name='view_shoe'),
    path('<int:pk>/edit_shoe', views.edit_shoe, name='edit_shoe'),
    path('<int:pk>/delete_shoe', views.delete_shoe, name='delete_shoe'),
]