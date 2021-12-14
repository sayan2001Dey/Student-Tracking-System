from django.urls import path
from . import views

app_name = 'cdc'

urlpatterns = [
    path('', views.dashboard, name='dashboard')
]