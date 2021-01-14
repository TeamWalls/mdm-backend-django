"""User Model"""

from django.db import models
from django.contrib.auth.models import AbstractUser , UserManager
from django.utils.translation import gettext_lazy as _
from mdm_inventory.utils.models import ModelDate


class User(ModelDate , AbstractUser):
    """User models.
        Extends from django's abstrac user, change the username fields to
        email and add some extra fields.
    """
    email = models.EmailField(
        _('Correo Electrónico'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    #permissions
    is_manager = models.BooleanField(_("Gerente") , default=False)
    is_cashier = models.BooleanField(_("Cajero") , default=False)
    is_superuser = models.BooleanField(_("Superusuario"), default=False)
    is_verified = models.BooleanField(
        _('Verificado'),
        default=False,
        help_text='Set true when the user have verified its email address.'
    )

    profile_picture = models.ImageField(
        _('Foto de Perfil'),
        upload_to='users/pictures/',
        default="users/pictures/user.png",
        max_length=250
    )

    def clean(self):
        super().clean()
        self.email = self.email.lower()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """Return username and email"""
        return f'{self.email} - {self.username}'

    def get_short_name(self):
        """Return username"""
        return self.username