from django.urls import path
from django.urls.conf import include
#from django.urls.resolvers import URLPattern

from .views import CampoCreate
from .views import CampoUpdate
from .views import CampoLista

from . views import CampoDelete
urlpatterns = [

    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
   

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
  

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
   

    path('lista/campo/', CampoLista.as_view(), name='lista-campo'),
]
