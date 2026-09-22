from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        MEDICO = 'MEDICO', 'Médico'
        RECEPCAO = 'RECEPCAO', 'Recepcionista'

    tipo = models.CharField(
        max_length=10,
        choices=TipoUsuario.choices,
        default=TipoUsuario.RECEPCAO,
    )

    def __str__(self):
        return self.username