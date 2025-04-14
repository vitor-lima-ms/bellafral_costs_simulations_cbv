from django.db import models

# Create your models here.

class Fralda(models.Model):
    modelo = models.CharField(verbose_name='Modelo', max_length=100)
    identificador = models.CharField(verbose_name='Identificador', max_length=100)
    tamanho = models.CharField(verbose_name='Tamanho', max_length=100)
    
    qtdCeluloseVirgem = models.DecimalField(verbose_name='Celulose virgem (Kg)', max_digits=10, decimal_places=4)
    qtdGel = models.DecimalField(verbose_name='Gel (Kg)', max_digits=10, decimal_places=4)
    qtdTnt750 = models.DecimalField(verbose_name='TNT 750 (m2)', max_digits=10, decimal_places=4)
    qtdTnt780 = models.DecimalField(verbose_name='TNT 780 (m2)', max_digits=10, decimal_places=4)
    qtdFitaAdesiva = models.DecimalField(verbose_name='Fita adesiva (m)', max_digits=10, decimal_places=4)
    qtdElastico = models.DecimalField(verbose_name='Elastico (Kg)', max_digits=10, decimal_places=4)
    qtdBarreira = models.DecimalField(verbose_name='Barreira (m2)', max_digits=10, decimal_places=4)
    qtdPolietileno750 = models.DecimalField(verbose_name='Polietileno 750 (Kg)', max_digits=10, decimal_places=4, default=0)
    qtdPolietileno780 = models.DecimalField(verbose_name='Polietileno 780 (Kg)', max_digits=10, decimal_places=4)
    qtdHotMelt = models.DecimalField(verbose_name='Hot-Melt (Kg)', max_digits=10, decimal_places=4)
    qtdPorPacote = models.IntegerField(verbose_name='Quantidade de fraldas por pacote')

    percentPerdas = models.DecimalField(verbose_name='Perdas (%)', max_digits=10, decimal_places=4)
    
    precoEmbalagem = models.DecimalField(verbose_name='Embalagem (R$)', max_digits=10, decimal_places=4)
    precoFardoEncarte = models.DecimalField(verbose_name='Saco para fardos/Encarte (R$)', max_digits=10, decimal_places=4)
    
    percentComissao = models.DecimalField(verbose_name='Comissão (%)', max_digits=10, decimal_places=4)
    percentImpostos = models.DecimalField(verbose_name='Impostos (%)', max_digits=10, decimal_places=4)
    percentFrete = models.DecimalField(verbose_name='Frete (%)', max_digits=10, decimal_places=4)
    percentMargem = models.DecimalField(verbose_name='Margem de contribuição (%)', max_digits=10, decimal_places=4)
    percentST = models.DecimalField(verbose_name='ST (%)', max_digits=10, decimal_places=4)

    def __str__(self):
        return f'Fralda: {self.modelo} {self.identificador} ({self.tamanho})'