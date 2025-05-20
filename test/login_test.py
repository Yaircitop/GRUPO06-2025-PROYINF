
import unittest
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from django.contrib.auth.hashers import make_password

class TestLoginEndpoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import os
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pagina.backend.settings")

        import django
        django.setup()
        # Conectar a MongoDB
        cls.client = MongoClient('mongodb+srv://juanito1080p:yF8rNzin3acyXk0w@cluster0.n4mdcsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        cls.db = cls.client['Cluster0']  
        cls.user_collection = cls.db['auth_user']
        cls.profile_collection= cls.db['signup_userprofile']  
        cls.base_url = "http://127.0.0.1:8000/login/"
        result= cls.user_collection.insert_one({"id":666,"username": "test@test.cl", "password": make_password("test"),"email":"test@test.cl","is_active": True})
        cls.user_id = result.inserted_id
        cls.profile_collection.insert_one({'user_id': cls.user_id,'run':"1.111.111-1"})

    def get_csrf_token(self, session):
        """Obtiene el token CSRF del formulario"""
        response = session.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        return csrf_token

    def test_login_valido(self):
        session = requests.Session()
        csrf_token = self.get_csrf_token(session)

        payload = {
            'csrfmiddlewaretoken': csrf_token,
            'username': 'test@test.cl',
            'password': 'test'
        }

        response = session.post(self.base_url, data=payload, allow_redirects=False)
        print(response)
        print("Login válido - Código esperado 302 - Código Obtenido:", response.status_code)
        self.assertEqual(response.status_code, 302)

    def test_login_invalido(self):
        session = requests.Session()
        csrf_token = self.get_csrf_token(session)

        payload = {
            'csrfmiddlewaretoken': csrf_token,
            'username': 'test@test.cl',
            'password': 'wrongpass'
        }

        response = session.post(self.base_url, data=payload)
        print(response)
        print("Login inválido - Código esperado 200 - Código Obtenido:", response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Usuario o contraseña incorrectos", response.text)

    @classmethod
    def tearDownClass(cls):
        # Limpiar datos insertados durante las pruebas
        cls.user_collection.delete_many({"username": {"$regex": "test"}})
        cls.profile_collection.delete_many({"run":"1.111.111-1"})
        cls.client.close()  # Cerrar la conexión con MongoDB
    

if __name__ == '__main__':
    unittest.main()
