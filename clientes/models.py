from django.db import models
from django.urls import reverse_lazy


class Cliente(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    telefone01 = models.CharField(max_length=30, null=True, blank=True)
    telefone02 = models.CharField(max_length=30, null=True, blank=True)
    veiculo = models.CharField(max_length=30, null=True, blank=True)
    rastreador = models.CharField(max_length=30, null=True, blank=True)
    instalado = models.BooleanField(default=False)
    data_instalcao = models.CharField(max_length=30, null=True, blank=True)
    retirado = models.BooleanField(default=False)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('clientes:clientes_detail', kwargs={'pk': self.pk})