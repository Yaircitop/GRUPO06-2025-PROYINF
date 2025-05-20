from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.login_url = reverse('login')
        cls.user_credentials = {
            'username': 'usuario@correo.com',
            'password': 'contraseñaCorrecta123'
        }
        cls.user = User.objects.create_user(
            username=cls.user_credentials['username'],
            password=cls.user_credentials['password']
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_login_exitoso(self):
        response = self.client.post(self.login_url, self.user_credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_password_vacio(self):
        response = self.client.post(self.login_url, {
            'username': 'usuario@correo.com',
            'password': ''
        }, follow=True)
        self.assertContains(response, "This field is required.", status_code=200)
