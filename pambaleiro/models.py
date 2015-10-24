# -*- coding: UTF-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


COUNTRY_CHOICES= (
    ('AO', 'Angola'),
    ('BR', 'Brasil'),
)
CITIES_CHOICES = (
    ('SRS', 'Santa Rita do Sapucai'),
    ('PA', 'Pouso Alegre'),
)

class Pambaleiro(models.Model):
    '''Essa classe representa a entidade Usuario'''
    user = models.OneToOneField(User, null=False)
    country = models.CharField(u'País', choices=COUNTRY_CHOICES, max_length=2, default='BR')
    city = models.CharField(u'CIdade', choices=CITIES_CHOICES, max_length=3, default='SRS')
    birth_date = models.DateField(u'Data de Nascimento', null=True)

    def __unicode__(self):
        return self.user.username

'''
#create our user object to attach to our Pambaleiro object
def create_pambaleiro_user_callback(sender, instance, **kwargs):
    pambaleiro, new = Pambaleiro.objects.get_or_create(user=instance)
post_save.connect(create_pambaleiro_user_callback, User)'''

