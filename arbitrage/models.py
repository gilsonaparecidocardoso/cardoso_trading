from datetime import datetime
from django.db import models

class Arbitragem(models.Model):
    price_a  = models.DecimalField(verbose_name="Valor A (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_a = models.CharField(verbose_name="Cripto A:", max_length=200, null=False, blank=False)
    price_b  = models.DecimalField(verbose_name="Valor B (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_b = models.CharField(verbose_name="Cripto B:", max_length=200, null=False, blank=False)
    data     = models.DateTimeField(verbose_name="Data:") #default=datetime.now() ao realizar migrations ele gera sempre um novo
    processo = models.CharField(verbose_name="Processo:", max_length=200, null=False, blank=False)

class Meta:
    ordering = ['data']

class ArbitragemCard(models.Model):
    price_a  = models.DecimalField(verbose_name="Valor A (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_a = models.CharField(verbose_name="Cripto A:", max_length=200, null=False, blank=False)
    price_b  = models.DecimalField(verbose_name="Valor B (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_b = models.CharField(verbose_name="Cripto B:", max_length=200, null=False, blank=False)
    data     = models.DateTimeField(verbose_name="Data:") #default=datetime.now() ao realizar migrations ele gera sempre um novo
    processo = models.CharField(verbose_name="Processo:", max_length=200, null=False, blank=False)

    @property
    def diferenca_cripto(self):
        if self.price_a > self.price_b:
            return self.price_a - self.price_b
        else:
            return self.price_b - self.price_a

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome