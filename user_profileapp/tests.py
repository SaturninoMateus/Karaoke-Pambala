from django.test import TestCase
from models import Usuario
import unittest

class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        self.saturnino = Usuario.objects.create(nome_usuario='s.nataniel10',
                                                nome=123,
                                                sobrenome='Mateus',
                                                email='s.nataniel10@gmail.com',
                                                data_nascimento='2000-12-30',
                                                pais='BR',
                                                cidade='SRS',
                                                senha='123')

    def testGet_nome(self):
        self.assertEquals(self.saturnino.get_nome(), 'Nome: 123')

    '''def testGet_nome_usuario(self):
        self.assertEquals(self.saturnino.get_nome_usuario(),'Nome de usuario: s.nataniel10')'''

