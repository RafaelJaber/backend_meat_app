import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.conf import settings


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome de Usuário', max_length=100,
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome Completo', max_length=150)
    address = models.CharField('Endereço', max_length=250, blank=True, null=True)
    is_active = models.BooleanField('Está ativo', default=True, blank=True)
    is_staff = models.BooleanField('Administrativo', default=False, blank=True)
    is_superuser = models.BooleanField('Super Usuário', default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.name.split()[0]

    def get_full_name(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
