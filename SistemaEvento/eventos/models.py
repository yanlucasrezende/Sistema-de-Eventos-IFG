from django.db import models

TIPO_EVENTO_CHOICES = [
    ('seminario', 'Seminário'),
    ('congresso', 'Congresso'),
    ('olimpiada', 'Olimpíada'),
    ('feira', 'Feira'),
    ('festival', 'Festival'),
    ('exposicao', 'Exposição'),
    ('encontro', 'Encontro'),
    ('curso', 'Curso'),
    ('treinamento', 'Treinamento'),
    ('outros', 'Outros'),
]

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    inscricao_inicio = models.DateField(blank=True, null=True)
    inscricao_fim = models.DateField(blank=True, null=True)
    link_inscricao = models.URLField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_EVENTO_CHOICES,
        default='outros'
    )
    # Novos campos:
    nome_local = models.CharField(max_length=255, blank=True, null=True)
    link_maps = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
