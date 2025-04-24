from django.contrib.auth import views as auth_views
from django.urls import path, include
from schools import views as school_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schools.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='schools/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', school_views.register, name='register'),
]
