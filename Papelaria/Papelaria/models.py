from django.db import models


class Autor(models.Model):
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    edicao = models.CharField(max_length=50, blank=True, null=True)
    editora = models.CharField(max_length=255, blank=True, null=True)
    ano_publicacao = models.PositiveIntegerField(blank=True, null=True)
    preco_capa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    autores = models.ManyToManyField(Autor, through='LivroAutores')

    def __str__(self):
        return self.titulo


class Estoque(models.Model):
    ENTRADA = 'entrada'
    SAIDA = 'saida'
    TIPO_MOVIMENTO_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída')
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='estoque')
    tipo_movimento = models.CharField(max_length=10, choices=TIPO_MOVIMENTO_CHOICES)
    quantidade = models.PositiveIntegerField(default=0)
    data_movimento = models.DateField()

    def save(self, *args, **kwargs):
        if self.tipo_movimento == self.ENTRADA:
            self.livro.quantidade = getattr(self.livro, 'quantidade', 0) + self.quantidade
        elif self.tipo_movimento == self.SAIDA:
            self.livro.quantidade = max(getattr(self.livro, 'quantidade', 0) - self.quantidade, 0)
        self.livro.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_movimento} - {self.livro.titulo} ({self.quantidade})"

class LivroAutores(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # Outros campos adicionais

    class Meta:
        unique_together = ['livro', 'autor']