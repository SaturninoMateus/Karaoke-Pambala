# -*- coding: UTF-8 -*-
from django.db import models
from user_profileapp.models import Artista, Usuario

class Musica(models.Model):
    '''Essa classe representa a entidade Musica'''
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(u'título', max_length=25)
    album = models.CharField(u'album', max_length=25)
    descricao = models.CharField(u'descrição', max_length=50)
    votacao = models.IntegerField(u'votos')
    letra = models.TextField(u'letra')
    audio = models.FileField(u'audio', upload_to=u'musicas')

    # Neste caso, uma musica_app poderá ter vários artistas
    artista = models.ManyToManyField(Artista)

    def __unicode__(self):
        return self.titulo


class Gravacao(models.Model):
    '''Essa classe representa a entidade Gravacao'''
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(u'descrição', max_length=150)
    audio = models.FileField(u'áudio de gravação', upload_to=u'audio_gravacoes')
    horario = models.DateTimeField(auto_now=True)
    musica = models.ForeignKey(Musica)
    usuario = models.ForeignKey(Usuario)


    def __unicode__(self):
        #se vc estudou python então sabe o que isso faz
        return self.musica.titulo

    class Meta:
        verbose_name_plural = "gravações"

class Comentario(models.Model):
    '''Essa classe representa a entidade Musica'''
    id = models.AutoField(primary_key=True)
    texto = models.TextField()
    horario = models.DateTimeField(auto_now=True)
    gravacao = models.ForeignKey(Gravacao)
    usuario = models.ForeignKey(Usuario)


    def __unicode__(self):
        #se vc estudou python então sabe o que isso faz
        return self.usuario.nome_usuario


