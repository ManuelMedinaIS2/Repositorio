from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.


class LoginTestCase(TestCase):
    """
    Test sencillos
    """

    fixtures = ['admin-data']

    def test_redirect_home_login(self):
        """
        Un usuario no logueado que accede a la pagina de inicio
        deberia ser redireccionado a la pagina de login
        """
        response = self.client.get('/')
        self.assertRedirects(response, '/login/?next=/')

    def test_login_admin(self):
        """
        Realiza el login del admin
        """
        login_state = self.client.login(username='admin', password='adminadmin')
        self.assertEqual(login_state, True, 'El login deberia funcionar porque existe el usuario')

    def test_login_fail(self):
        """
        Un usuario no existente no deberia poder realizar el login
        """
        login_state = self.client.login(username='random', password='randomrandom')
        self.assertEqual(login_state, False, 'El login no deberia funcionar porque el usuario no existe')

    def test_redirect_login_home(self):
        """
        Un usuario que realiza el login accediendo la pagina de login directamente
        deberia ser luego redirigo a la pagina de inicio
        """
        response = self.client.post('/login/', {'username': 'admin', 'passsword': 'adminadmin'})
        self.assertRedirects(response, '/')