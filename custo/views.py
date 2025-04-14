from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from custo.models import Custo

# Create your views here.
    
class CreateCusto(CreateView):
    model = Custo
    fields = '__all__'
    template_name = 'create_custo.html'
    success_url = reverse_lazy('custo:list_custos')

class ListCusto(ListView):
    model = Custo
    template_name = 'list_custos.html'
    context_object_name = 'custos'

class DetailCusto(DetailView):
    model = Custo
    template_name = 'detail_custo.html'
    context_object_name = 'custo'

class UpdateCusto(UpdateView):
    model = Custo
    fields = '__all__'
    template_name = 'update_custo.html'
    success_url = reverse_lazy('simulacao:index')

class DeleteCusto(DeleteView):
    model = Custo
    template_name = 'delete_custo.html'
    success_url = reverse_lazy('simulacao:index')
