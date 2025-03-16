from django.urls import path
from .views import EventoListView, EventoCreateView, EventoUpdateView, EventoDeleteView

urlpatterns = [
    path('', EventoListView.as_view(), name='evento_list'),
    path('novo/', EventoCreateView.as_view(), name='evento_create'),
    path('editar/<int:pk>/', EventoUpdateView.as_view(), name='evento_edit'),
    path('excluir/<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),
]
