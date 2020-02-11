from django.db import models
from perfis.models import Perfil


# Create your models here.
class Tweet(models.Model):
    conteudo = models.CharField(max_length=200, verbose_name='Conteúdo')
    publicado_em = models.DateTimeField(verbose_name='Publicado em:', auto_now_add=True)
    autor = models.ForeignKey(Perfil, related_name='tweets', on_delete=models.CASCADE)
    likes = models.ManyToManyField(Perfil, related_name='tweets_liked')

    def __str__(self):
        return self.conteudo
    # return f' {self.conteudo} ({self.autor})'


class Comentario(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.CharField(max_length=200, verbose_name='Conteúdo')
    publicado_em = models.DateTimeField(verbose_name='Publicado em:', auto_now_add=True)
    autor = models.ForeignKey(Perfil, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
