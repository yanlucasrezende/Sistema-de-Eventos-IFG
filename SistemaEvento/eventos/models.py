from django.db import models
from django.contrib.auth.models import User  # Import necessário

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

class Atividade(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    local = models.CharField(max_length=255)
    limite_vagas = models.IntegerField(blank=True, null=True)
    TIPO_ATIVIDADE_CHOICES = [
        ('alimentacao', 'Alimentação'),
        ('apresentacao_artistica', 'Apresentação Artística'),
        ('apresentacao_trabalho_cientifico', 'Apresentação de Trabalho Científico'),
        ('cerimonia', 'Cerimônia'),
        ('coloquio', 'Colóquio'),
        ('conferencia', 'Conferência'),
        ('curso', 'Curso'),
        ('divulgacao', 'Divulgação'),
        ('encontro', 'Encontro'),
        ('espetaculo', 'Espetáculo'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_ATIVIDADE_CHOICES)
    
    # Novo campo para armazenar os usuários inscritos na atividade
    inscritos = models.ManyToManyField(User, blank=True, related_name='atividades_inscritas')

    def __str__(self):
        return f"{self.evento.nome} - {self.get_tipo_display()}"
