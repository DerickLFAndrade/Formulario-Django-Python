from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividades

from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('lista-campo')


class AtividadesCreate(CreateView):
    model = Atividades
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

#####Update#####

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class AtividadeUpdate(UpdateView):
    model = Atividades
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


#####Delete#####

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class AtividadeDelete(DeleteView):
    model = Atividades
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

#####LISTA#####


class CampoLista(ListView):
    model = Campo
    template_name = 'cadastros/listas/listaUsuario.html'
    


class AtividadeLista(ListView):
    model = Atividades
    template_name = 'cadastros/listas/listaAtividade.html'
    
