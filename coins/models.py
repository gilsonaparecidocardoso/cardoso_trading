from datetime import datetime
from django.db import models
from datetime import datetime

class MoedasADM(models.Model):
    email   = models.EmailField((""), max_length=254)
    name    = models.CharField(verbose_name="Nome:", max_length=200, null=False, blank=False)

class Moedas(models.Model):
    symbol      = models.CharField    (verbose_name="Símbolo:", max_length=200, null=False, blank=False)
    name        = models.CharField    (verbose_name="Nome:", max_length=200, null=False, blank=False)
    platforms   = models.CharField    (verbose_name="Plataforma:", max_length=200, null=False, blank=False)
    currency    = models.DecimalField (verbose_name="Valor:", max_digits=10, decimal_places=2, null=False, blank=False)
    data        = models.DateTimeField(verbose_name="Data:") #default=datetime.now() Gera sempre um registro a mais ao migrar

    def __str__(self):
        return self.name