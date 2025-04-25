from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Atleta, Treinador, Patrocinador
from django.utils.translation import gettext_lazy as _


# Mixin para aplicar classes do Tailwind a todos os campos
class TailwindWidgetMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tailwind_class = "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_classes} {tailwind_class}".strip()
            # Se não houver placeholder definido, usa o label
            if not field.widget.attrs.get("placeholder"):
                field.widget.attrs["placeholder"] = field.label


# ================================
# Formulários de Criação
# ================================


class CustomUserCreationForm(UserCreationForm, TailwindWidgetMixin):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={"placeholder": "Email"})
    )
    nome = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Nome"}),
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
        required=True,
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirme a Senha"}),
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "nome", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Criptografa a senha
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm, TailwindWidgetMixin):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={"placeholder": "Senha"}),
    )

    def clean(self):
        email = self.cleaned_data.get("username")  # aqui continua sendo "username"
        password = self.cleaned_data.get("password")
        if email and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError("Email ou senha incorretos.")
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class AtletaForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário de cadastro de atleta."""

    class Meta:
        model = Atleta
        fields = [
            "nome",
            "data_nascimento",
            "classificacao_funcional",
            "nados",
            "historico_competicoes",
        ]


class TreinadorForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário de cadastro de treinador."""

    class Meta:
        model = Treinador
        fields = ["nome", "especializacoes", "atletas_treinados", "historico"]


class PatrocinadorForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário de cadastro de patrocinador."""

    class Meta:
        model = Patrocinador
        fields = ["nome", "empresa"]


# ================================
# Formulários de Atualização
# ================================


class CustomUserUpdateForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário para atualização dos dados do usuário."""

    class Meta:
        model = CustomUser
        fields = ["email", "nome"]


class AtletaUpdateForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário para atualização dos dados do atleta."""

    class Meta:
        model = Atleta
        fields = [
            "nome",
            "data_nascimento",
            "classificacao_funcional",
            "nados",
            "historico_competicoes",
        ]


class TreinadorUpdateForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário para atualização dos dados do treinador."""

    class Meta:
        model = Treinador
        fields = ["nome", "especializacoes", "atletas_treinados", "historico"]


class PatrocinadorUpdateForm(forms.ModelForm, TailwindWidgetMixin):
    """Formulário para atualização dos dados do patrocinador."""

    class Meta:
        model = Patrocinador
        fields = ["nome", "empresa"]
