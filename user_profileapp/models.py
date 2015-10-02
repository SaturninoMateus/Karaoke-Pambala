# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


########################################################################################################
ESCOLHA_DE_PAISES = (
    ('AO', 'Angola'),
    ('BR', 'Brasil'),
)
ESCOLHA_DE_CIDADES = (
    ('SRS', 'Santa Rita do Sapucai'),
    ('PA', 'Pouso Alegre'),
)
########################################################################################################
class Usuario(AbstractBaseUser, models.Model):
    '''Essa classe representa a entidade Usuario'''

    #cada usuario terá um nickname e email únicos
    nome_usuario = models.CharField(u'nome de usuario', primary_key=True, max_length=15, unique=True, db_index=True)
    nome = models.CharField(u'nome', max_length=15)
    sobrenome = models.CharField(u'sobrenome', max_length=15)
    email = models.EmailField(u'email', unique=True)
    #profile_photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    data_nascimento = models.DateField(u'data de nascimento',null=False)
    pais = models.CharField(u'pais', max_length=2,
                            choices=ESCOLHA_DE_PAISES,
                            default='BR')
    cidade = models.CharField(u'cidade', max_length=3,
                              choices=ESCOLHA_DE_CIDADES,
                              default='SRS')
    senha = models.CharField(u'senha', max_length=20)

    #USERNAME_FIELD, também funciona como identificador único para o modelo usuario no django, este campo tem que ser "unique=True"
    USERNAME_FIELD = 'nome_usuario'
    REQUIRED_FIELDS = ['nome_usuario','email']

    def __unicode__(self):
        #se vc estudou python então sabe o que isso faz
        return self.nome_usuario
###############################################################################################
class Artista(models.Model):
    '''Essa classe representa a entidade Artista'''
    id = models.AutoField(primary_key=True)
    nome = models.CharField(u'nome', max_length=20)
    sobrenome = models.CharField(u'sobrenome', max_length=20)
    biografia = models.TextField(u'biografia')

    def __unicode__(self):
        #se vc estudou python então sabe o que isso faz
        return self.nome+' '+self.sobrenome
###############################################################################################