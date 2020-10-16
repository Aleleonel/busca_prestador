from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import PrestadorForm
from .models import Prestador


def home(request):
    template_name = 'buscaprest/home.html'
    return render(request, template_name)


def my_static(request):
    template_name = 'buscaprest/estatico.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')
    if search and search2:
        objects = Prestador.objects.filter(categoria__icontains=search, cidade__icontains=search2)
        context = {
            'object_list': objects
        }
        return render(request, template_name, context)
    elif search:
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


def lista(request):
    template_name = 'buscaprest/buscaprest_lista.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')
    if search and search2:
        objects = Prestador.objects.filter(categoria__icontains=search, cidade__icontains=search2)
        context = {
            'object_list': objects
        }
        return render(request, template_name, context)

    elif search:
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


def prestadores_add(request):
    template_name = 'buscaprest/buscaprest_form.html'
    return render(request, template_name)


class PrestadorCreate(CreateView):
    model = Prestador
    template_name = 'buscaprest/buscaprest_form.html'
    form_class = PrestadorForm


class PrestadorUpdate(UpdateView):
    model = Prestador
    template_name = 'buscaprest/buscaprest_form.html'
    form_class = PrestadorForm
