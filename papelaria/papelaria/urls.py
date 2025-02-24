
from django.contrib import admin
from django.urls import path
from website import views
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('livros/', views.livros_list, name='livros_list'),
    path('livros_create/', views.livros_create, name='livros_create'),

    path('autores/', views.autores_list, name='autores_list'),
    path('autores/novo/', views.autores_create, name='autores_create'),
    path('autores/editar/<int:pk>/', views.autores_update, name='autores_update'),
    path('autores/excluir/<int:pk>/', views.autores_delete, name='autores_delete'),




    path('vendas/', views.vendas_list, name='vendas_list'),

    path('estoque/', views.estoque_list, name='estoque_list'),
]
