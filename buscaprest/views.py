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
        obj = Prestador.objects.filter(categoria__icontains=search)
        context = {
            'obj': obj
        }
        return render(request, template_name, context)
    else:
        obj = Prestador.objects.all().order_by('-pk')
        context = {'obj': obj}
    return render(request, template_name, context)


def prestadores_detail(request, pk):
    model = Prestador
    template_name = 'buscaprest/buscaprest_detail.html'
    detail = Prestador.objects.get(pk=pk)
    context = {'detail': detail}
    return render(request, template_name, context)

