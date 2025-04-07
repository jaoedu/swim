from django.urls import path
from .views import NoticiaCreateView, NoticiaDetailView, NoticiaListView

urlpatterns = [
    path("listagem/", NoticiaListView.as_view(), name="noticia_lista"),  # Lista de notícias
    path(  "nova/", NoticiaCreateView.as_view(), name="noticia_criar"),  # Criar nova notícia
    path( "<int:pk>/", NoticiaDetailView.as_view(), name="noticia_detalhe"),  # Detalhe de uma notícia
]
    