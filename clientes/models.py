from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):

    RETIRADO_CHOICES = (
        ('SIM', 'sim'),
        ('NAO', 'nao')
    )

    INSTALADO_CHOICES = (
        ('SIM', 'sim'),
        ('NAO', 'nao')
    )
    nome = models.CharField(max_length=60, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    telefone01 = models.CharField(max_length=30, null=True, blank=True)
    telefone02 = models.CharField(max_length=30, null=True, blank=True)
    veiculo = models.CharField(max_length=30, null=True, blank=True)
    rastreador = models.CharField(max_length=30, null=True, blank=True)
    instalado = models.CharField(max_length=3, choices=INSTALADO_CHOICES)
    data_instalcao = models.DateTimeField(auto_created=False, auto_now_add=False)
    retirado = models.CharField(max_length=3, choices=RETIRADO_CHOICES)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('clientes:clientes_detail', kwargs={'pk': self.pk})