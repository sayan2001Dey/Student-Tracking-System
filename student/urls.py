from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('add_activity/', views.add_activity, name="add_activity"),
    path('edit_activity/<id>/', views.edit_activity, name="edit_activity"),
]