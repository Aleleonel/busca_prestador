from django.urls import path
from . import views

app_name = 'buscaprest'

urlpatterns = [
    path('', views.home, name='home'),
    path('estatico/', views.my_static, name='my_static'),
    path('lista/', views.lista, name='buscaprest_lista'),
    path('<int:pk>/', views.prestadores_detail, name='prestadores_detail'),
    path('<int:pk>/edit/', views.PrestadorUpdate.as_view(), name='prestadores_edit'),
    path('add/', views.PrestadorCreate.as_view(), name='prestadores_add'),
]