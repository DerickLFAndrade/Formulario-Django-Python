from django.urls import path
from django.urls.conf import include
#from django.urls.resolvers import URLPattern
from .views import PaginaInicial, listaU, modelo

urlpatterns = [
    #path('endereço/', MinhaView.as.view(), name='nome-da-url')
    path('', PaginaInicial.as_view(), name='index'),
    path('modelo/', modelo.as_view(), name='modelo'),
    path('listaUsuaraios/', listaU.as_view(), name='lista'),
    path('',include('cadastros.urls')),
   
]
