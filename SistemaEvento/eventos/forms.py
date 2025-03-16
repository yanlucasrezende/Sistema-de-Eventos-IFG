from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nome',
            'data_inicio',
            'data_fim',
            'inscricao_inicio',
            'inscricao_fim',
            'link_inscricao',
            'descricao',
            'ativo',
            'tipo',
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'inscricao_inicio': forms.DateInput(attrs={'type': 'date'}),
            'inscricao_fim': forms.DateInput(attrs={'type': 'date'}),
            'tipo': forms.RadioSelect(),  # Exibe como botões de rádio
        }
