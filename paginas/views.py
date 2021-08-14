from django.views.generic import TemplateView

# Create your views here.


class PaginaInicial(TemplateView):
    template_name = "cadastroU.html"

class listaU(TemplateView):
    template_name = "listaU.html"

class modelo(TemplateView):
    template_name = ("modelo.html")
