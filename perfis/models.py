from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
class Perfil(models.Model):
    usuario = models.ForeignKey(
        auth_models.User,
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )
    bio = models.CharField(
        max_length=200,
        help_text='Escreva sobre você'
    )
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username
