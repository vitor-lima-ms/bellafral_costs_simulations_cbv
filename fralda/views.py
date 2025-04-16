from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from fralda.models import Fralda

# Create your views here.

class CreateFralda(CreateView):
    model = Fralda
    fields = '__all__'
    template_name = 'create_fralda.html'
    success_url = reverse_lazy('fralda:list_fraldas')

class ListFralda(ListView):
    model = Fralda
    template_name = 'list_fraldas.html'
    context_object_name = 'fraldas'

class DetailFralda(DetailView):
    model = Fralda
    template_name = 'detail_fralda.html'
    context_object_name = 'fralda'

class UpdateFralda(UpdateView):
    model = Fralda
    fields = '__all__'
    template_name = 'update_fralda.html'
    success_url = reverse_lazy('fralda:list_fraldas')

class DeleteFralda(DeleteView):
    model = Fralda
    template_name = 'delete_fralda.html'
    success_url = reverse_lazy('fralda:list_fraldas')
