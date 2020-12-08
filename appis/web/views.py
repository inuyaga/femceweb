from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class InicioWebView(TemplateView):
    template_name = "web/inicio.html"