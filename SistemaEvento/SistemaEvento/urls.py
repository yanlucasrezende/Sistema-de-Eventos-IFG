from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views import custom_logout  # Importa a view customizada de logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('eventos/', include('eventos.urls')),
    path('usuarios/', include('usuarios.urls')),
]