from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Prestador


def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def lista(request):
    template_name = 'buscaprest/buscaprest_lista.html'
    search = request.GET.get('search')
    if search:
        objects = Prestador.objects.filter(categoria__icontains=search)
        context = {
            'object_list': objects
        }
        return render(request, template_name, context)
    else:
        objects = Prestador.objects.all()
        context = {
            'object_list': objects
        }

    return render(request, template_name, context)


def prestadores_detail(request, pk):
    template_name = 'buscaprest/buscaprest_detail.html'
    obj = Prestador.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

