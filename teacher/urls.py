from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('add_activity/', views.add_activity, name="add_activity"),
    path('all_students/', views.all_students, name="all_students"),
    path('add_marks/<id_student>/', views.add_marks, name="add_marks"),
    path('add_attendance/<id_student>/', views.add_attendance, name="add_attendance"),
]