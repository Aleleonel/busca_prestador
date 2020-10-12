from django.urls import path
from . import views

app_name = 'buscaprest'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('<int:pk>/', views.prestadores_detail, name='prestadores_detail'),
]