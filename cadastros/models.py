from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50) 
    descricao = models.CharField(max_length=50, verbose_name="descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividades(models.Model):
    numero = models.IntegerField(max_length=11,  verbose_name='Número')
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=1, max_digits=4)
    detalhes = models.CharField(max_length=100)

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__ (self):
        return "{} ({})".format(self.nome, self.campo.nome)
