from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('eventos/', include('eventos.urls')),
    path('usuarios/', include('usuarios.urls')),
]