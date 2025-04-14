from django.urls import path
from custo.views import CreateCusto
from custo.views import ListCusto
from custo.views import UpdateCusto
from custo.views import DeleteCusto
from custo.views import DetailCusto
app_name = 'custo'

urlpatterns = [
    path('create/', CreateCusto.as_view(), name='create_custo'),

    path('list/', ListCusto.as_view(), name='list_custos'),

    path('detail/<int:pk>/', DetailCusto.as_view(), name='detail_custo'),

    path('update/<int:pk>/', UpdateCusto.as_view(), name='update_custo'),

    path('delete/<int:pk>/', DeleteCusto.as_view(), name='delete_custo'),
]