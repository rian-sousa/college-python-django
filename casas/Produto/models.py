from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    nSerie = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    anoDoProduto = models.CharField(max_length=4)
    quantidade = models.CharField(max_length=6)

def __str__(self):
    return self.nome
