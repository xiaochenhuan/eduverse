from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schools/', views.school_list, name='school_list'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('districts/<int:pk>/', views.district_detail, name='district_detail'),
    path('enrollment-chart/', views.enrollment_by_state, name='enrollment_chart'),
]
