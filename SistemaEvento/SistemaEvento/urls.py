from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rota do admin
    path('admin/', admin.site.urls),
    
    # Rota de login (seu template de login)
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    
    # Inclui as rotas do app 'eventos'
    path('eventos/', include('eventos.urls')),
]
