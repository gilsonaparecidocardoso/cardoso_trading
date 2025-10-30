from django.db import models

class Produto(models.Model):
    nome      = models.CharField (verbose_name="Nome:", max_length=200, null=False, blank=False)
    descricao = models.CharField (verbose_name="Descrição:", max_length=200, null=False, blank=False)
    preco     = models.DecimalField (max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name