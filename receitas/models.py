from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200, null=False, blank=False,)
    ingrediantes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=200)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
