from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo

from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-campo')


#####Update#####

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/formup.html'
    success_url = reverse_lazy('lista-campo')





#####Delete#####

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('lista-campo')



#####LISTA#####


class CampoLista(ListView):
    model = Campo
    template_name = 'cadastros/listas/listaUsuario.html'
    


    
