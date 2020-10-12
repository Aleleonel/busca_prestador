from django.db import models


class Prestador(models.Model):
    categoria = models.CharField(max_length=60, null=True, blank=True)
    prestador = models.CharField(max_length=60, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=True, blank=True)
    cep = models.CharField(max_length=60, null=True, blank=True)
    telefone2 = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.prestador

    class Meta:
        db_table = 'prestador'