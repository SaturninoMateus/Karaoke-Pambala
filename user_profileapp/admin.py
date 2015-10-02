from django.contrib import admin
from models import Usuario, Artista


class UsuarioAdmin(admin.ModelAdmin):
    fields = ('email', 'nome', 'sobrenome','nome_usuario', 'senha','data_nascimento', 'pais', 'cidade')

class ArtistaAdmin(admin.ModelAdmin):
    fields = ('nome', 'sobrenome', 'biografia')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Artista, ArtistaAdmin)