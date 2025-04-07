from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "conteudo","tags", "imagem_capa"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título da notícia"}
            ),
            "conteudo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escreva o conteúdo aqui...",
                }
            ),
           
            "tags": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tags separadas por vírgula",
                }
            ),
            "imagem_capa": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_tags(self):
        tags = self.cleaned_data.get("tags", [])
        if isinstance(tags, str):  # Converte string separada por vírgulas em lista
            tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
        return tags
