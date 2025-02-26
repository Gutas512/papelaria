from django import forms
from Papelaria.models import *

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'isbn', 'edicao', 'editora', 'ano_publicacao', 'preco_capa', 'categoria', 'autores']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome_completo', 'nacionalidade', 'biografia']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['livro', 'tipo_movimento', 'quantidade', 'data_movimento']