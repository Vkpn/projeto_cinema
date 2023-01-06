from django.db import models


class Horarios(models.Model):
    horarios = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.horarios


class Filme(models.Model):
    nome = models.CharField(max_length=50)
    lancamento = models.DateField(null=False)
    diretor = models.CharField(default='Não Especificado', max_length=20)
    genero = models.CharField(max_length=20)
    capa = models.ImageField(upload_to='capa_filme')
    idioma = models.CharField(max_length=10)
    horarios_filmes = models.ManyToManyField(Horarios)
    sala = models.CharField( max_length=10)
    sinopse = models.TextField()

    def __str__(self) -> str:
        return self.nome