from django.urls import path
from . import views as v

app_name = 'clientes'

urlpatterns = [
    path('', v.clientes_list, name='clientes_list'),

    path('<int:pk>/', v.clientes_detail, name='clientes_detail'),
    path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='clientes_edit'),
    path('add/', v.ClienteCreate.as_view(), name='clientes_add'),
]
