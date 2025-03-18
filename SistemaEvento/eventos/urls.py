from django.urls import path
from .views import (
    EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView,
    AtividadeListView, AtividadeCreateView, AtividadeUpdateView, AtividadeDeleteView
)

urlpatterns = [
    path('', EventoListView.as_view(), name='evento_list'),
    path('novo/', EventoCreateView.as_view(), name='evento_create'),
    path('editar/<int:pk>/', EventoUpdateView.as_view(), name='evento_edit'),
    path('excluir/<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),
    path('<int:evento_pk>/atividades/', AtividadeListView.as_view(), name='atividade_list'),
    path('<int:evento_pk>/atividades/novo/', AtividadeCreateView.as_view(), name='atividade_create'),
    path('atividades/editar/<int:pk>/', AtividadeUpdateView.as_view(), name='atividade_edit'),
    path('atividades/excluir/<int:pk>/', AtividadeDeleteView.as_view(), name='atividade_delete'),
]
