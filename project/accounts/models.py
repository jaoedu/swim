from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password, check_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError("O email deve ser fornecido")
        if not nome:
            raise ValueError("O nome deve ser fornecido")
        if not password:
            raise ValueError("A senha deve ser fornecida")

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)  # Usa a senha corretamente
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, nome, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return self.email


class Nado(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    classificacao_funcional = models.CharField(max_length=50)
    nados = models.ManyToManyField(Nado, blank=True)
    historico_competicoes = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.nome


class Treinador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    especializacoes = models.CharField(max_length=100)
    atletas_treinados = models.ManyToManyField(Atleta, blank=True)
    historico = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.nome


class Patrocinador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
