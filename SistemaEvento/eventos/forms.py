from django import forms
from .models import Evento, Atividade

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
            'nome_local',  # novo
            'link_maps'    # novo
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'inscricao_inicio': forms.DateInput(attrs={'type': 'date'}),
            'inscricao_fim': forms.DateInput(attrs={'type': 'date'}),
            'tipo': forms.RadioSelect(),  # Exibe como botões de rádio
        }

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['descricao', 'data_inicio', 'data_fim', 'local', 'tipo']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'tipo': forms.RadioSelect(),  # Apresenta as opções como botões de rádio
        }
