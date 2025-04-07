from django.views.generic import TemplateView
from news.models import Noticia  # Importa o model da app news

class HomeView(TemplateView):
    template_name = "home/home.html"  # Caminho para o template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona as notícias ordenadas pela data de publicação (mais recentes primeiro)
        context['noticias'] = Noticia.objects.all().order_by('-data_publicacao')
        return context
