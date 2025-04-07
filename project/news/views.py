from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Noticia
from .forms import NoticiaForm


class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = "news/create_news.html"
    success_url = reverse_lazy("home")  # Redireciona após criar com sucesso

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class NoticiaListView(ListView):
    model = Noticia
    template_name = "news/list_news.html"
    context_object_name = "noticias"
    ordering = ["-data_publicacao"]


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "news/noticia_detail.html"
    context_object_name = "noticia"
