from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class Curso(models.Model):
    
    titulo = models.CharField(max_length=60)
    tempo = models.IntegerField()
    valor = models.IntegerField()
    descricao = models.CharField(max_length=260)
    conteudo = models.CharField(max_length=260)
    
