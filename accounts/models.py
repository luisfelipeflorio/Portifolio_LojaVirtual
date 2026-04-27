from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel


class CustomUser(TimeStampedModel, AbstractUser):
    phone = models.CharField('telefone', max_length=20, blank=True)

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'


class Address(TimeStampedModel):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='addresses', verbose_name='usuário')
    street = models.CharField('rua', max_length=255)
    number = models.CharField('número', max_length=20)
    complement = models.CharField('complemento', max_length=100, blank=True)
    neighborhood = models.CharField('bairro', max_length=100)
    city = models.CharField('cidade', max_length=100)
    state = models.CharField('estado', max_length=2)
    zip_code = models.CharField('CEP', max_length=10)
    is_default = models.BooleanField('endereço padrão', default=False)

    class Meta:
        verbose_name = 'endereço'
        verbose_name_plural = 'endereços'

    def __str__(self):
        return f'{self.street}, {self.number} - {self.city}'
