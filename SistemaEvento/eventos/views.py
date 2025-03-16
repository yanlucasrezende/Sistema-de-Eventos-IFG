from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm

class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

    def dispatch(self, request, *args, **kwargs):
        # Garante que apenas usuários autenticados possam acessar
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class EventoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento_list')

    def test_func(self):
        return self.request.user.is_staff

class EventoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('evento_list')

    def test_func(self):
        return self.request.user.is_staff

class EventoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy('evento_list')

    def test_func(self):
        return self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)
