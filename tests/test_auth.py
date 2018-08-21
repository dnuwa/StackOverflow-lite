import unittest
import json
from app.views import api, app
from app.models import User
from run import api


class TestStackOverFlowliteUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        self.user = {
            "display_name": "godfrey",
            "email": "godfrey@gmail.com",
            "password": "12"
        }
        self.usermisses = {
            "email": "godfrey@gmail.com",
            "password": "12"
        }
        self.user_2 = {
            "display_name": "daniel",
            "email": "daniel@gmail.com",
            "password": "1234"
        }
        self.userlogin = {
            "display_name": "daniel",
            "password": "1234"
        }

    def test_user_sigin_up_successfully(self):
        response = self.app.post(
            '/api/v1/subscribers', content_type="application/json", data=json.dumps(self.user))
        self.assertEqual(
            response.json, {"msg": "you have signed up as godfrey"})
        self.assertEqual(response.status_code, 201)

    def test_user_misses_field_at_signup(self):
        response = self.app.post(
            '/api/v1/subscribers', content_type="application/json", data=json.dumps(self.usermisses))
        self.assertEqual(
            response.json, {"error": "You have missed out some info, check the keys too"})
        self.assertEqual(response.status_code, 400)

    def test_user_attempts_signup_with_existing_account(self):
        response = self.app.post(
            '/api/v1/subscribers', content_type="application/json", data=json.dumps(self.user_2))
        self.assertEqual(
            response.json, {"msg": "This account already exists"})
        self.assertEqual(response.status_code, 400)

    def test_getting_all_signedup_users(self):
        response = self.app.get('/api/v1/subscribers',
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_sigin_successfully(self):
        response = self.app.post(
            '/api/v1/login', content_type="application/json", data=json.dumps(self.userlogin))
        self.assertEqual(response.json, {"msg": "You are logged in as daniel"})
        self.assertEqual(response.status_code, 200)

    