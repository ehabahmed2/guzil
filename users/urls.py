from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.admin_dash, name='admin_dashboard'),
]
