from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):

    CARGO_GERENTE = 'G'
    CARGO_VENDEDOR = 'V'

    CHOICES_CARGO = (
        (CARGO_VENDEDOR, 'Vendedor'),
        (CARGO_GERENTE, 'Gerente'),
    )

    cargo = models.CharField(
        max_length=1,
        choices=CHOICES_CARGO
    )

    
