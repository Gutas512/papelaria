from django.contrib import admin
from django.urls import path
from website import views
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('autores/', listar_autores, name='autor_list'),
    path('autores/<int:pk>/', detalhe_autor, name='autor_detail'),
    path('autores/novo/', criar_autor, name='autor_create'),
    path('autores/<int:pk>/editar/', atualizar_autor, name='autor_update'),
    path('autores/<int:pk>/excluir/', deletar_autor, name='autor_delete'),

    path('', views.index, name='index'),

    path('livros/', views.livro_list, name='livro_list'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/editar/', views.livro_edit, name='livro_edit'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),

    path('estoque/', views.estoque_list, name='estoque_list'),
    path('estoque/novo/', views.estoque_create, name='estoque_create'),
    path('estoque/<int:pk>/', views.estoque_detail, name='estoque_detail'),
    path('estoque/<int:pk>/editar/', views.estoque_edit, name='estoque_edit'),
    path('estoque/<int:pk>/deletar/', views.estoque_delete, name='estoque_delete'),

]
