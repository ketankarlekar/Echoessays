from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),

    path('logout/', views.custom_logout, name='users-logout'),
]
