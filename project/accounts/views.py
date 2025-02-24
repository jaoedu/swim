from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser, Atleta, Treinador, Patrocinador
from .forms import CustomUserCreationForm,CustomAuthenticationForm, AtletaForm, TreinadorForm, PatrocinadorForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages
import logging
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic.edit import UpdateView, DeleteView
from .forms import CustomUserUpdateForm, AtletaUpdateForm, TreinadorUpdateForm, PatrocinadorUpdateForm
from django.contrib.auth import login


logger = logging.getLogger(__name__)

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("selecao_success")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Cadastro realizado com sucesso!")
        return response


class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "accounts/user_update.html"
    success_url = reverse_lazy("profile")  # Altere para a URL desejada (ex: página de perfil)

    def test_func(self):
        # Apenas o próprio usuário pode atualizar seus dados
        return self.request.user.pk == self.get_object().pk


class CustomUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Em vez de excluir permanentemente, desativa a conta definindo is_active=False.
    """
    model = CustomUser
    template_name = "accounts/user_confirm_deactivate.html"
    success_url = reverse_lazy("login")  # Após desativar, redireciona para a página de login

    def test_func(self):
        # Apenas o próprio usuário pode desativar sua conta
        return self.request.user.pk == self.get_object().pk

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)

class selectionView(TemplateView):
    template_name = "accounts/selecao_conta.html"


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        """Faz login e adiciona um log."""
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, "Login realizado com sucesso!")
        return redirect("home")  # Redireciona para a home após login bem-sucedido


class AtletaCreateView(CreateView):
    model = Atleta
    form_class = AtletaForm
    template_name = "accounts/atleta_cadastrar.html"
    success_url = reverse_lazy("atleta_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AtletaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Atleta
    form_class = AtletaUpdateForm
    template_name = "accounts/update_atleta.html"
    success_url = reverse_lazy(
        "atleta_detail"
    )  # Altere para a URL desejada (ex: página de detalhes ou listagem)

    def test_func(self):
        atleta = self.get_object()
        return atleta.user == self.request.user


class AtletaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Em vez de excluir o registro de atleta, desativa a conta do usuário associado.
    """

    model = Atleta
    template_name = "accounts/atleta_confirm_deactivate.html"
    success_url = reverse_lazy("login")

    def test_func(self):
        atleta = self.get_object()
        return atleta.user == self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Desativa o usuário associado (soft delete)
        user = self.object.user
        user.is_active = False
        user.save()
        return redirect(self.success_url)


class TreinadorCreateView(CreateView):
    model = Treinador
    form_class = TreinadorForm
    template_name = "accounts/treinador_cadastrar.html"
    success_url = reverse_lazy("treinador_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TreinadorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Treinador
    form_class = TreinadorUpdateForm
    template_name = "accounts/update_treinador.html"
    success_url = reverse_lazy("treinador_detail")

    def test_func(self):
        treinador = self.get_object()
        return treinador.user == self.request.user


class TreinadorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Desativa o treinador (através do usuário associado) em vez de excluir permanentemente.
    """

    model = Treinador
    template_name = "accounts/treinador_confirm_deactivate.html"
    success_url = reverse_lazy("login")

    def test_func(self):
        treinador = self.get_object()
        return treinador.user == self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        user.is_active = False
        user.save()
        return redirect(self.success_url)


class PatrocinadorCreateView(CreateView):
    model = Patrocinador
    form_class = PatrocinadorForm
    template_name = "accounts/patrocinador_cadastrar.html"
    success_url = reverse_lazy("patrocinador_success")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PatrocinadorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patrocinador
    form_class = PatrocinadorUpdateForm
    template_name = "accounts/update_patrocinador.html"
    success_url = reverse_lazy("patrocinador_detail")

    def test_func(self):
        patrocinador = self.get_object()
        return patrocinador.user == self.request.user

class PatrocinadorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Em vez de excluir permanentemente, desativa a conta do usuário associado ao patrocinador.
    """
    model = Patrocinador
    template_name = "accounts/patrocinador_confirm_deactivate.html"
    success_url = reverse_lazy("login")

    def test_func(self):
        patrocinador = self.get_object()
        return patrocinador.user == self.request.user

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        user.is_active = False
        user.save()
        return redirect(self.success_url)
