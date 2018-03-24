from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User


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
  

    def test_login_admin(self):
        """
        Realiza el login del admin
        """

    def test_login_fail(self):
        """
        Un usuario no existente no deberia poder realizar el login
        """

    def test_redirect_login_home(self):
        """
        Un usuario que realiza el login accediendo la pagina de login directamente
        deberia ser luego redirigo a la pagina de inicio
        """
