from django.contrib.auth.backends import BaseBackend
from .models import CustomUser


class EmailCPFBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(
                password
            ):  # Utiliza o método de verificação da senha
                return user
        except CustomUser.DoesNotExist:
            return None
