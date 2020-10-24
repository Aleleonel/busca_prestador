from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import ClienteForm
from .models import Cliente


def clientes_list(request):
    template_name = 'clientes/clientes_list.html'
    search = request.GET.get('search')
    search2 = request.GET.get('search2')
    if search and search2:
        obj = Cliente.objects.filter(veiculo__icontains=search, rastreador__icontains=search2)
        context = {
            'obj': obj
        }
        return render(request, template_name, context)
    elif search:
        obj = Cliente.objects.filter(veiculo__icontains=search)
        context = {
            'obj': obj
        }
        return render(request, template_name, context)
    elif search2:
        obj = Cliente.objects.filter(rastreador__icontains=search2)
        context = {
            'obj': obj
        }
        return render(request, template_name, context)
    else:
        obj = Cliente.objects.all()
        context = {
            'obj': obj
        }
    return render(request, template_name, context)


def clientes_detail(request, pk):
    template_name = 'clientes/clientes_detail.html'
    obj = Cliente.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def clientes_add(request):
    template_name = 'clientes/cliente_form.html'
    return render(request, template_name)


class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    form_class = ClienteForm


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    form_class = ClienteForm
