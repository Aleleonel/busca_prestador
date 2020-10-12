from django.contrib import admin
from .models import Prestador


class ListaPrestador(admin.ModelAdmin):
    list_display = (
        'id',
        'categoria',
        'prestador',
        'endereco',
        'bairro',
        'cidade',
        'cep',
        'telefone2'
    )
    list_filter = ("categoria",)
    search_fields = ('cidade', 'categoria',)


admin.site.register(Prestador, ListaPrestador)
