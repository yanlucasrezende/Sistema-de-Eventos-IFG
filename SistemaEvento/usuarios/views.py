from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import UserCreationFormWithRole

class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = UserCreationFormWithRole
    template_name = 'usuarios/user_create.html'
    success_url = reverse_lazy('evento_list')

    def test_func(self):
         return self.request.user.is_staff

    def form_valid(self, form):
         response = super().form_valid(form)
         role = form.cleaned_data.get('role')
         if role == 'admin':
             self.object.is_staff = True
         else:
             self.object.is_staff = False
         self.object.save()
         return response