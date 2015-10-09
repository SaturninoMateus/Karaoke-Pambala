from django import test
from user_profileapp import models

class UsuarioTestCase(test.TestCase):
    def teste_usuario_deve_ter_nome(self):
        fields = models.Usuario._meta.get_all_field_names()
        self.assertIn('nome', fields)
