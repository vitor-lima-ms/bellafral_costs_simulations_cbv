from django.urls import path
from simulacao.views import CreateSimulacao
from simulacao.views import DeleteSimulacao
from simulacao.views import ListSimulacao
from simulacao.views import download_simulation

app_name = 'simulacao'

urlpatterns = [
    path('', ListSimulacao.as_view(), name='index'),

    path('create/', CreateSimulacao.as_view(), name='create_simulacao'),

    path('delete/<int:pk>/', DeleteSimulacao.as_view(), name='delete_simulacao'),

    path('download/<int:pk>/', download_simulation, name='download_simulation'),
]