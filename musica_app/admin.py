from django.contrib import admin
from models import Musica, Gravacao, Comentario


class MusicaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'album', 'descricao','audio', 'votacao', 'letra')

class GravacaoAdmin(admin.ModelAdmin):
    fields = ('descricao', 'audio', 'musica', 'usuario')

class ComentarioAdmin(admin.ModelAdmin):
    fields = ('usuario', 'gravacao', 'texto')


admin.site.register(Musica,MusicaAdmin)
admin.site.register(Gravacao, GravacaoAdmin)
admin.site.register(Comentario, ComentarioAdmin)