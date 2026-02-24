from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_student, name='add_student'),
    path('result/<int:student_id>/', views.result, name='result'),
    path('logout/', views.logout_view, name='logout'),
]