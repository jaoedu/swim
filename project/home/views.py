from django.views.generic import TemplateView
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = "home/home.html"  # Caminho para o template


