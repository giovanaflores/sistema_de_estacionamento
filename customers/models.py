from django.db import models
from django.contrib.auth.models import User

from .validator import cpf_validation, name_validation, phone_validation


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,  # impede que um objeto seja deletado se existir outro objeto relacionado com ele
        blank=True,
        null=True,
        related_name='customers',
        verbose_name='Usuário',
    )
    name = models.CharField(max_length=100, verbose_name='Nome', validators=[name_validation])
    
    cpf = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='CPF',
        unique=True,
        validators=[cpf_validation],
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
        validators=[phone_validation],
    )
    created_at = models.DateTimeField(  # armazena quando o registro foi criado
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(  # DateTimeField armazena data e hora
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
