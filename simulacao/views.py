from django.views.generic import CreateView
from django.views.generic import View
from django.views.generic import DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
import csv

from simulacao.models import Simulacao

import simulacao.functions as functions

# Create your views here.

class CreateSimulacao(CreateView):
    model = Simulacao
    fields = ['custoObj', 'fraldaObj']
    template_name = 'create_simulacao.html'
    success_url = reverse_lazy('simulacao:index')

class ListSimulacao(View):
    def get(self, request):
        simulacoes = Simulacao.objects.all()

        for simulacao in simulacoes:
            functions.calcular_custo_unitario_total_por_componente(simulacao)
            functions.calcular_custo_total_sem_perdas(simulacao)
            functions.calcular_custo_total_com_perdas(simulacao)
            functions.calcular_custo_pacote(simulacao)
            functions.calcular_custo_unitario_final(simulacao)
            functions.calcular_preco_venda(simulacao)
            functions.calcular_preco_venda_unitario(simulacao)
            functions.calcular_preco_venda_st(simulacao)
            functions.calcular_preco_venda_unitario_st(simulacao)

        return render(request, 'list_simulacoes.html', {'simulacoes': simulacoes})
    
class DeleteSimulacao(DeleteView):
    model = Simulacao
    template_name = 'delete_simulacao.html'
    success_url = reverse_lazy('simulacao:index')

def download_simulation(request, pk):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="simulation.csv"'

    csv_writer = csv.writer(response)

    simulation = get_object_or_404(Simulacao, pk=pk)

    csv_writer.writerow(
        [
            'Item',
            'Quantidade',
            'Custo unitário',
            'Custo total',
        ]
    )

    csv_writer.writerow(
        [
            'Celulose virgem (Kg)',
            simulation.fraldaObj.qtdCeluloseVirgem,
            simulation.custoObj.custoCeluloseVirgem,
            round(simulation.fraldaObj.qtdCeluloseVirgem * simulation.custoObj.custoCeluloseVirgem, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Gel (Kg)',
            simulation.fraldaObj.qtdGel,
            simulation.custoObj.custoGel,
            round(simulation.fraldaObj.qtdGel * simulation.custoObj.custoGel, 4),
        ]
    )

    csv_writer.writerow(
        [
            'TNT - Filtrante - 162mm (m2)',
            simulation.fraldaObj.qtdTnt162,
            simulation.custoObj.custoTnt162,
            round(simulation.fraldaObj.qtdTnt162 * simulation.custoObj.custoTnt162, 4),
        ]
    )

    csv_writer.writerow(
        [
            'TNT - Filtrante - 750mm (m2)',
            simulation.fraldaObj.qtdTnt750,
            simulation.custoObj.custoTnt750,
            round(simulation.fraldaObj.qtdTnt750 * simulation.custoObj.custoTnt750, 4),
        ]
    )
    
    csv_writer.writerow(
        [
            'TNT - Filtrante - 780mm (m2)',
            simulation.fraldaObj.qtdTnt780,
            simulation.custoObj.custoTnt780,
            round(simulation.fraldaObj.qtdTnt780 * simulation.custoObj.custoTnt780, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Fita adesiva - Tape (Kg)',
            simulation.fraldaObj.qtdFitaAdesiva,
            simulation.custoObj.custoFitaAdesiva,
            round(simulation.fraldaObj.qtdFitaAdesiva * simulation.custoObj.custoFitaAdesiva, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Elástico - Elastano - Lycra (Kg)',
            simulation.fraldaObj.qtdElastico,
            simulation.custoObj.custoElastico,
            round(simulation.fraldaObj.qtdElastico * simulation.custoObj.custoElastico, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Barreira (m2)',
            simulation.fraldaObj.qtdBarreira,
            simulation.custoObj.custoBarreira,
            round(simulation.fraldaObj.qtdBarreira * simulation.custoObj.custoBarreira, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Polietileno - Filme - 162mm (m2)',
            simulation.fraldaObj.qtdPolietileno162,
            simulation.custoObj.custoPolietileno162,
            round(simulation.fraldaObj.qtdPolietileno162 * simulation.custoObj.custoPolietileno162, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Polietileno - Filme - 750mm (m2)',
            simulation.fraldaObj.qtdPolietileno750,
            simulation.custoObj.custoPolietileno750,
            round(simulation.fraldaObj.qtdPolietileno750 * simulation.custoObj.custoPolietileno750, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Polietileno - Filme - 780mm (Kg)',
            simulation.fraldaObj.qtdPolietileno780,
            simulation.custoObj.custoPolietileno780,
            round(simulation.fraldaObj.qtdPolietileno780 * simulation.custoObj.custoPolietileno780, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Hot-Melt Construção (Kg)',
            simulation.fraldaObj.qtdHotMelt,
            simulation.custoObj.custoHotMelt,
            round(simulation.fraldaObj.qtdHotMelt * simulation.custoObj.custoHotMelt, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Custo total s/ perdas (R$)',
            simulation.fraldaCustoTotalSemPerdas,
        ]
    )

    csv_writer.writerow(
        [
            'Perdas (%)',
            simulation.fraldaObj.percentPerdas,
        ]
    )

    csv_writer.writerow(
        [
            'Custo total com perdas (R$)',
            simulation.fraldaCustoTotalComPerdas,
        ]
    )


    csv_writer.writerow(
        [
            'Quantidade de peças por pacote',
            simulation.fraldaObj.qtdPorPacote,
        ]
    )

    csv_writer.writerow(
        [
            'Embalagem (R$)',
            simulation.fraldaObj.precoEmbalagem,
        ]
    )

    csv_writer.writerow(
        [
            'Saco para fardos (R$)',
            simulation.fraldaObj.precoFardoEncarte,
        ]
    )

    csv_writer.writerow(
        [
            'Custo do pacote (R$)',
            simulation.fraldaCustoPacote,
        ]
    )

    csv_writer.writerow(
        [
            'Custo unitário final (R$)',
            simulation.fraldaCUF,
        ]
    )

    csv_writer.writerow(
        [
            'Comissão (%)',
            simulation.fraldaObj.percentComissao,
        ]
    )

    csv_writer.writerow(
        [
            'Impostos (%)',
            simulation.fraldaObj.percentImpostos,
        ]
    )

    csv_writer.writerow(
        [
            'Frete (%)',
            simulation.fraldaObj.percentFrete,
        ]
    )

    csv_writer.writerow(
        [
            'Margem de contribuição (%)',
            simulation.fraldaObj.percentMargem,
        ]
    )

    csv_writer.writerow(
        [
            'ST (%)',
            simulation.fraldaObj.percentST,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda (R$)',
            simulation.precoVenda,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda unitário (R$)',
            simulation.precoVendaUnitario,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda com ST (R$)',
            simulation.precoVendaST,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda unitário com ST (R$)',
            simulation.precoVendaUnitarioST,
        ]
    )

    return response