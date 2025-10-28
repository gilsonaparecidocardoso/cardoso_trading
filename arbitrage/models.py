from datetime import date
from django.db import models

class Arbitragem(models.Model):
    price_a  = models.DecimalField(verbose_name="Valor A (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_a = models.CharField(verbose_name="Cripto A:", max_length=200, null=False, blank=False)
    price_b  = models.DecimalField(verbose_name="Valor B (R$):", max_digits=10, decimal_places=2, null=False, blank=False)    
    cripto_b = models.CharField(verbose_name="Cripto B:", max_length=200, null=False, blank=False)
    data     = models.DateField(verbose_name="Data:", default=date.today)
    processo = models.CharField(verbose_name="Processo:", max_length=200, null=False, blank=False)

class Meta:
    ordering = ['data']