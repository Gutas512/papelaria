from django import forms
from papelaria.models import *

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = [
            'liv_titulo', 'liv_ISBN', 'liv_edicao', 'liv_editora',
            'liv_ano_publicacao', 'liv_preco_capa', 'liv_categoria', 'liv_quant'
        ]

class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['aut_nome', 'aut_nacionalidade', 'aut_biografia']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['id_livro', 'est_entrada', 'est_saida']

class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['id_livro', 'ven_quant_vendida', 'ven_data_venda', 'ven_valor']
