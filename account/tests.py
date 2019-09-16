import bcrypt
import json
import jwt

from datetime      import timedelta
from .models       import Accounts

from django.test   import Client, TestCase
from unittest.mock import patch, MagicMock

class SignUpTest(TestCase):
    def setUp(self):

        password  = bytes('baby2019', 'UTF-8')
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        Accounts.objects.create(
            email    = 'babytiger@gmail.com',
            name     = 'Baby',
            password = hashed_pw.decode('UTF-8'),
        )


    def tearDown(self):
        Accounts.objects.filter(name='test').delete()

    # Test Valid Case
    def test_valid_account(self):
        c = Client()
        
        test = {
            'email': 'werbnb@gmail.com',
            'name' : 'admin',
            'password' : 'werbnb2019',
        }
        response = c.post('/account/signup', json.dumps(test), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Test Invalid Cases
    def test_blank_email(self):
        c = Client()

        test = {
            'name' : 'Baby',
            'password' : '1234',
            'email' : '',
        }
        response = c.post('/account/signup', json.dumps(test), content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_blank_password(self):
        c = Client()

        test = {
            'email' : 'happycoding@gmail.com',
            'name'  : '1234',
            'password' : '',
        }
        response = c.post('/account/signup', json.dumps(test), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_exist_email(self):
        c = Client()

        test = {
             'email' : 'babytiger@gmail.com',
             'name' : 'Baby',
             'password' : 'baby2019',
        }
        response = c.post('/account/signup', json.dumps(test), content_type='application/json')
        self.assertEqual(response.status_code, 400)


class LogInTest(TestCase):
    def setUp(self):
        c = Client()
        
        password  = bytes('baby2019', 'UTF-8')
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        Accounts.objects.create(
            email    = 'babytiger@gmail.com',
            password = hashed_pw.decode('UTF-8')
        )

    def tealDown(self):
        Accounts.objects.filter(email='babytiger@gmail.com').delete()

    # Test Valid Case
    def test_valid_account(self):
        c = Client()
        
        test = {
            'email' : 'babytiger@gmail.com',
            'password' : 'baby2019'
        }
        
        response = c.post('/account/login', json.dumps(test), content_type='application/json')
        access_token = response.json()['access_token']

        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'access_token' : access_token})

    # Test Invalid Account
    def test_invalid_account(self):
        c = Client()

        test = {
            'email' : 'notexist@gmail.com',
            'password' : '1234567890'
        }
        response = c.post('/account/login', json.dumps(test), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_invalid_password(self):
        c = Client()

        test = {
            'email' : 'babytiger@gmail.com',
            'password' : '12121212',
        }
        response = c.post('/account/login', json.dumps(test), content_type='application/json')
        self.assertEqual(response.status_code, 401)




