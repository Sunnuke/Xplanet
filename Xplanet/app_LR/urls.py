from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('Register', views.register),
    path('Login', views.login),
    path('Logout', views.logout),
]