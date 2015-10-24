# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.core.exceptions import ValidationError




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

class Usuario(AbstractBaseUser):
    '''Essa classe representa a entidade Usuario'''

    #cada usuario terá um nickname e email únicos
    nome_usuario = models.CharField(u'nome de usuario', primary_key=True, max_length=15, unique=True, db_index=True)
    nome = models.CharField(u'nome', max_length=15)
    sobrenome = models.CharField(u'sobrenome', max_length=15)
    email = models.EmailField(u'email', unique=True)
    #profile_photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    data_nascimento = models.DateField(u'data de nascimento',null=False)
    is_active = models.BooleanField(default=True)
    pais = models.CharField(u'pais', max_length=2,
                            choices=ESCOLHA_DE_PAISES,
                            default='BR')
    cidade = models.CharField(u'cidade', max_length=3,
                              choices=ESCOLHA_DE_CIDADES,
                              default='SRS')
    senha = models.CharField(u'senha', max_length=20)

    #USERNAME_FIELD, também funciona como identificador único para o modelo usuario no django, este campo tem que ser "unique=True"
    USERNAME_FIELD = 'nome_usuario'
    PASSWORD_FIELD = 'senha'
    REQUIRED_FIELDS = ['nome_usuario','email']

    def __unicode__(self):
        #se vc estudou python então sabe o que isso faz
        return self.nome_usuario

    def get_nome(self):
        return 'Nome: %s' % (str(self.nome))

    def get_nome_usuario(self):
        return 'Nome de usuario: %s' % (str(self.nome_usuario))

    """def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        '''
        for x in '0123456789':
            if x in self.nome:git
                raise ValidationError('erro')'''
        self.nome = str(self.nome)

        super(Usuario, self).save(*args, **kwargs)"""

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
