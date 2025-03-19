from django.urls import path
from .views import (
    EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView,
    AtividadeListView, AtividadeCreateView, AtividadeUpdateView, AtividadeDeleteView,
    InscreverAtividadeView, InscritosListView, RemoverInscritoView
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
    path('inscrever/<int:pk>/', InscreverAtividadeView.as_view(), name='inscrever_atividade'),
    path('inscritos/<int:atividade_pk>/', InscritosListView.as_view(), name='inscritos_list'),
    path('inscritos/<int:atividade_pk>/remover/<int:user_pk>/', RemoverInscritoView.as_view(), name='remover_inscrito'),
]
