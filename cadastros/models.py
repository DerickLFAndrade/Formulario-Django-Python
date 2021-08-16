from django.db import models
from django.db.models.fields import DecimalField

from cpf_field.models import CPFField



# Create your models here.
class Campo(models.Model):
    nome = models.EmailField(max_length=50, verbose_name="E-mail")
    descricao = CPFField(verbose_name = "CPF")
    

   

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

