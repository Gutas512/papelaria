from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from Papelaria.models import *
from Papelaria.forms import *
from django.views.generic import *

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'website/autor_list.html', {'autores': autores})

def detalhe_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'website/autor_detail.html', {'autor': autor})

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'website/autor_form.html', {'form': form})

def atualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'website/autor_form.html', {'form': form})

def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    return render(request, 'website/autor_confirm_delete.html', {'autor': autor})

def index(request):
    return render(request, 'website/index.html')

# Listar todos os livros
def livro_list(request):
    livros = Livro.objects.all()
    return render(request, 'website/livro_list.html', {'livros': livros})

# Detalhes de um livro
def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'website/livro_detail.html', {'livro': livro})

# Criar novo livro
def livro_create(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')  # Redireciona para a lista de livros
    else:
        form = LivroForm()
    return render(request, 'website/livro_form.html', {'form': form})

# Editar um livro existente
def livro_edit(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_detail', pk=livro.pk)  # Redireciona para os detalhes do livro
    else:
        form = LivroForm(instance=livro)
    return render(request, 'website/livro_form.html', {'form': form})

# Excluir um livro
def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect('livro_list')  # Redireciona para a lista de livros
    return render(request, 'webiste/livro_confirm_delete.html', {'livro': livro})


def estoque_list(request):
    # Obtemos todos os registros de estoque
    movimentos = Estoque.objects.all()
    return render(request, 'website/list.html', {'movimentos': movimentos})

def estoque_create(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')  # Redireciona para a lista de movimentos de estoque
    else:
        form = EstoqueForm()

    return render(request, 'website/form.html', {'form': form})

def estoque_detail(request, pk):
    movimento = get_object_or_404(Estoque, pk=pk)
    return render(request, 'website/detail.html', {'movimento': movimento})


def estoque_edit(request, pk):
    movimento = get_object_or_404(Estoque, pk=pk)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=movimento)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')  # Redireciona para a lista de movimentos de estoque
    else:
        form = EstoqueForm(instance=movimento)

    return render(request, 'website/form.html', {'form': form})

def estoque_delete(request, pk):
    movimento = get_object_or_404(Estoque, pk=pk)
    movimento.delete()
    return redirect('estoque_list')