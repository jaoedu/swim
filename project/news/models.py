from django.db import models
from django.conf import settings


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(max_length=10000)
    data_publicacao = models.DateTimeField(auto_now_add=True)
      # Define a data no momento da criação
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário customizado
        on_delete=models.CASCADE,
    )
    tags = models.JSONField(
        default=list
    )  # Pode ser uma lista de strings ou outra abordagem
    imagem_capa = models.ImageField(upload_to="noticias/capas/", null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("noticia_detalhe", args=[str(self.id)])
