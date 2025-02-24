from django.shortcuts import render, get_object_or_404, redirect
from papelaria.models import *
from papelaria.forms import *

# Views para Livros

def livros_list(request):
    livros = Livros.objects.all()
    return render(request, 'livros_list.html', {'livros': livros})

def livros_create(request):
    if request.method == "POST":
        # Obtém os dados do formulário
        liv_titulo = request.POST.get('liv_titulo')
        liv_ISBN = request.POST.get('liv_ISBN')
        liv_edicao = request.POST.get('liv_edicao')
        liv_editora = request.POST.get('liv_editora')
        liv_ano_publicacao = request.POST.get('liv_ano_publicacao')
        liv_preco_capa = request.POST.get('liv_preco_capa')
        liv_categoria = request.POST.get('liv_categoria')
        liv_quant = request.POST.get('liv_quant')
        autor_id = request.POST.get('Autor')

        # Cria o livro no banco de dados
        novo_livro = Livros(
            liv_titulo=liv_titulo,
            liv_ISBN=liv_ISBN,
            liv_edicao=liv_edicao,
            liv_editora=liv_editora,
            liv_ano_publicacao=liv_ano_publicacao,
            liv_preco_capa=liv_preco_capa,
            liv_categoria=liv_categoria,
            liv_quant=liv_quant,
            autor_id=autor_id
        )
        novo_livro.save()

        return redirect('livros_list')  # Redireciona para a lista de livros após salvar

    # Passa a lista de autores para o template
    autores = Autor.objects.all()
    return render(request, 'livros_create.html', {'autores': autores})


def livros_update(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros_list')
    else:
        form = LivrosForm(instance=livro)
    return render(request, 'livros_form.html', {'form': form})

def livros_delete(request, pk):
    livro = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros_list')
    return render(request, 'livros_confirm_delete.html', {'livro': livro})

# Views para Autores


def autores_list(request):
    autores = Autor.objects.all()  # Recupera todos os autores do banco de dados
    return render(request, 'autores_list.html', {'autores': autores})

def autores_create(request):
    if request.method == "POST":
        nome = request.POST.get("aut_nome")
        nacionalidade = request.POST.get("aut_nacionalidade")
        biografia = request.POST.get("aut_biografia")


        novo_autor = Autor(aut_nome=nome, aut_nacionalidade=nacionalidade, aut_biografia=biografia)
        novo_autor.save()

        return redirect("/autores/")  #

    return render(request, "autores_form.html")

def autores_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutoresForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores_list')
    else:
        form = AutoresForm(instance=autor)
    return render(request, 'autores_form.html', {'form': form})


def autores_delete(request, pk):
    autor = get_object_or_404(Autor, id_autores=pk)  # Recupera o autor pelo ID ou retorna 404
    if request.method == 'POST':
        autor.delete()  # Deleta o autor
        return redirect('autores_list')  # Redireciona para a lista de autores após a exclusão
    return render(request, 'autores_delete.html', {'autor': autor})

# Views para Estoque

def estoque_list(request):
    livros = Livros.objects.all()
    return render(request, 'estoque_list.html', {'livros': livros})

def estoque_create(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')
    else:
        form = EstoqueForm()
    return render(request, 'estoque_form.html', {'form': form})

def estoque_update(request, pk):
    item = get_object_or_404(Estoque, pk=pk)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')
    else:
        form = EstoqueForm(instance=item)
    return render(request, 'estoque_form.html', {'form': form})

def estoque_delete(request, pk):
    item = get_object_or_404(Estoque, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('estoque_list')
    return render(request, 'estoque_confirm_delete.html', {'item': item})

# Views para Vendas

def vendas_list(request):
    livros = Livros.objects.all()
    return render(request, 'vendas_list.html', {'livros': livros})

def vendas_create(request):
    if request.method == 'POST':
        form = VendasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendas_list')
    else:
        form = VendasForm()
    return render(request, 'vendas_form.html', {'form': form})

def vendas_update(request, pk):
    venda = get_object_or_404(Vendas, pk=pk)
    if request.method == 'POST':
        form = VendasForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('vendas_list')
    else:
        form = VendasForm(instance=venda)
    return render(request, 'vendas_form.html', {'form': form})

def vendas_delete(request, pk):
    venda = get_object_or_404(Vendas, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('vendas_list')
    return render(request, 'vendas_confirm_delete.html', {'venda': venda})

def index(request):
    return render(request, 'index.html')
