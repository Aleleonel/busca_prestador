from django.shortcuts import render
from django.views import generic
from .models import Prestador


def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def lista(request):
    model = Prestador
    template_name = 'buscaprest/buscaprest_lista.html'
    search = request.GET.get('search')

    if search:
        buscando = Prestador.objects.filter(categoria__icontains=search)
        context = {
            'buscando': buscando
        }
        return render(request, template_name, context)

    else:
        obj = Prestador.objects.all().order_by('-pk')
        context = {
            'obj': obj
        }

    return render(request, template_name, context)