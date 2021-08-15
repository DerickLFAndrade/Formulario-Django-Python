from django.urls import path
#from django.urls.resolvers import URLPattern

from .views import CampoCreate, AtividadesCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoLista, AtividadeLista

from . views import CampoDelete, AtividadeDelete
urlpatterns = [

    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadesCreate.as_view(), name='cadastrar-atividade'),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),

    path('lista/campo/', CampoLista.as_view(), name='lista-campo'),
    path('lista/atividade/', AtividadeLista.as_view(), name='lista-atividade'),


]
