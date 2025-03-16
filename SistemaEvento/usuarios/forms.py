from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithRole(UserCreationForm):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('visitante', 'Visitante'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'role')
