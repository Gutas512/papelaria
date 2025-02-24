from django.db import models

class Autor(models.Model):
    id_autores = models.AutoField(primary_key=True)
    aut_nome = models.CharField(max_length=75)
    aut_nacionalidade = models.CharField(max_length=20)
    aut_biografia = models.CharField(max_length=50)

    class Meta:
        db_table = 'Autores'

    def __str__(self):
        return self.aut_nome


class Livros(models.Model):
    liv_titulo = models.CharField(max_length=200)
    liv_ISBN = models.CharField(max_length=13)
    liv_edicao = models.CharField(max_length=50)
    liv_editora = models.CharField(max_length=100)
    liv_ano_publicacao = models.IntegerField()  # Certifique-se de que este campo existe
    liv_preco_capa = models.DecimalField(max_digits=5, decimal_places=2)
    liv_categoria = models.CharField(max_length=100)
    liv_quant = models.IntegerField()
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Livros'

    def __str__(self):
        return self.liv_titulo



class Estoque(models.Model):
    id_livro = models.ForeignKey(
        Livros,
        on_delete=models.CASCADE
    )
    est_entrada = models.DateField(
        null=False,
        blank=False
    )
    est_saida = models.DateField(
        null=False,
        blank=False
    )
    def __str__(self):
        return self.id_livro

class Vendas(models.Model):
    id_venda = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    id_livro = models.ForeignKey(
        Livros,
        on_delete=models.CASCADE
    )
    ven_quant_vendida = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    ven_data_venda = models.DateField(
        null=False,
        blank=False
    )
    ven_valor = models.FloatField(
        default=0,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.id_venda