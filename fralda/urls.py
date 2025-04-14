from django.urls import path
from fralda.views import CreateFralda
from fralda.views import ListFralda
from fralda.views import UpdateFralda
from fralda.views import DeleteFralda
from fralda.views import DetailFralda

app_name = 'fralda'

urlpatterns = [
    path('create/', CreateFralda.as_view(), name='create_fralda'),
    
    path('list/', ListFralda.as_view(), name='list_fraldas'),

    path('detail/<int:pk>/', DetailFralda.as_view(), name='detail_fralda'),

    path('update/<int:pk>/', UpdateFralda.as_view(), name='update_fralda'),

    path('delete/<int:pk>/', DeleteFralda.as_view(), name='delete_fralda'),
]
