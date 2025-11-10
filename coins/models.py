from django.db import models

STATUS = (
    ('A', 'Ativo'),
    ('I', 'Inativo'),)

class MoedasADM(models.Model):
    email   = models.EmailField((''), max_length=254)
    name    = models.CharField(verbose_name='Nome', max_length=200, null=False, blank=False)
    status  = models.CharField(verbose_name='Status', max_length=1, choices=STATUS, default='I')
    photo   = models.ImageField(upload_to='', null=True, blank=True)

class Moedas(models.Model):
    idn         = models.CharField    (verbose_name='Idn', max_length=200)
    symbol      = models.TextField    (verbose_name='Simbolo', max_length=200, null=False, blank=False)
    name        = models.CharField    (verbose_name='Nome', max_length=200, null=False, blank=False)
    platforms   = models.TextField    (verbose_name='Plataforma', max_length=200, null=False, blank=False)
    currency    = models.DecimalField (verbose_name='Valor', max_digits=10, decimal_places=2, null=False, blank=False)
    data        = models.DateTimeField(verbose_name='Data') #default=datetime.now() Gera sempre um registro a mais ao migrar

    def __str__(self):
        return self.name

    @property
    def teste_metodo(self):
        return self.name - self.currency

    
# class MoedasImport(models.Model):
#     idn         = models.CharField    (verbose_name="Idn:", max_length=200)
#     symbol      = models.TextField    (verbose_name="Símbolo:", max_length=200, null=False, blank=False)
#     name        = models.CharField    (verbose_name="Nome:", max_length=200, null=False, blank=False)
#     platforms   = models.TextField    (verbose_name="Plataforma:", max_length=200, null=False, blank=False)
#     currency    = models.DecimalField (verbose_name="Valor:", max_digits=10, decimal_places=2, null=False, blank=False)
#     quantidade  = models.IntegerField (verbose_name="Quantidade:")

#     @property
#     def quantidade(self):
#         return self.quantidade , 'R$'