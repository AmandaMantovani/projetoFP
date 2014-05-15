from django.db import models

class Caixa(models.Model):
    tipo = models.CharField(max_length='100', 
        blank=False,  #permitir nulo
        null=False)

    descricao = models.CharField(max_length='100', 
        blank=True, 
        null=True)

    valor = models.DecimalField(max_digits=20, decimal_places=2,
        default=0)

    pagseguro = models.CharField(max_length='200', 
        blank=True, 
        null=True)

    data = models.CharField(max_length='200', 
        blank=True, 
        null=True)
