from django.db import models

from custo.models import Custo
from fralda.models import Fralda

# Create your models here.

class Simulacao(models.Model):
    custoObj = models.ForeignKey(verbose_name='Custo', on_delete=models.CASCADE, to=Custo)
    fraldaObj = models.ForeignKey(verbose_name='Fralda', on_delete=models.CASCADE, to=Fralda)

    celuloseVirgemCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    gelCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt162CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt750CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt780CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fitaAdesivaCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    elasticoCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    barreiraCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno162CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno750CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno780CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    hotMeltCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    
    fraldaCustoTotalSemPerdas = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCustoTotalComPerdas = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCustoPacote = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCUF = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)

    precoVenda = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaUnitario = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaST = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaUnitarioST = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)

    def __str__(self):
        return f'{self.fraldaObj.modelo} - {self.custoObj.identificador}'
