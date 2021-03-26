from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_from_index_to_login, name='index'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
]