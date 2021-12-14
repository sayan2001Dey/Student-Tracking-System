from django.urls import path
from . import views

app_name = 'activity'

urlpatterns = [
    path('delete/<id_activity>/', views.delete_activity, name='delete_activity')
]