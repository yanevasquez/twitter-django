from django.contrib import admin
from publicacoes import models


# Register your models here.
@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'conteudo',
        'autor',
        'publicado_em',

    )

    def has_delete_permission(self, request, obj=None):
        perfil = request.user.perfil_set.first()
        return (
                request.user.groups.filter(name='Moderador').exists() or
                obj and obj.autor == perfil
        )

    def has_change_permission(self, request, obj=None):
        perfil = request.user.perfil_set.first()
        return obj and obj.autor == perfil


# admin.site.register(models.Tweet, TweetAdmin)
admin.site.register(models.Comentario)
