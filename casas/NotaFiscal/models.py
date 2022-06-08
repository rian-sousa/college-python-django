from django.db import models

class NotaFiscal(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    cpf = models.CharField(max_length=11)
    nSerie = models.CharField(max_length=20)

def __str__(self):
    return self.nome
