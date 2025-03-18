from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Evento, Atividade
from .forms import EventoForm, AtividadeForm

# --------------------------
# Views para Eventos
# --------------------------

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

# --------------------------
# Views para Atividades
# --------------------------

class AtividadeListView(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'eventos/atividade_list.html'
    context_object_name = 'atividades'

    def get_queryset(self):
        evento_id = self.kwargs.get('evento_pk')
        return Atividade.objects.filter(evento_id=evento_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evento'] = Evento.objects.get(pk=self.kwargs.get('evento_pk'))
        return context

class AtividadeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Atividade
    form_class = AtividadeForm
    template_name = 'eventos/atividade_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        evento_id = self.kwargs.get('evento_pk')
        form.instance.evento_id = evento_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('atividade_list', kwargs={'evento_pk': self.kwargs.get('evento_pk')})

class AtividadeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Atividade
    form_class = AtividadeForm
    template_name = 'eventos/atividade_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('atividade_list', kwargs={'evento_pk': self.object.evento_id})

class AtividadeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Atividade

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse(status=200)
