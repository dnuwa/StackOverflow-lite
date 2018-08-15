import unittest
import json
from views import api, app
from models import User, Qn, Answer
from run import *


class TestStackOverFlowliteApi(unittest.TestCase):

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

        self.qn1 = {
            "qn_id": 2,
            "qn": "is a string a data type?",
            "display_name": "daniel"
        }
        self.qn2 = {"qn": "is a string a data type?","display_name": "daniel"
        }

        self.qn3 = {'display_name': 'daniel', 'qn_id': 1, 'qn': 'what is a datastructure'}
        self.qn4 = {'display_name': 'johnie', 'qn_id': 4, 'qn': 'what is a computer science'}

        self.answer = {"ans_id": 1,"ans": "dictionaries"}
        self.answer2 = {"ans_id": 2, "ans": "some_text"}

    def test_user_sigin_up_successfully(self):
        response = self.app.post(
            '/api/v1/subscribers', content_type="application/json", data=json.dumps(self.user))
        self.assertEqual(
            response.json, {"message": "you have signed up as godfrey"})
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
        response = self.app.get('/api/v1/subscribers', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_user_sigin_successfully(self):
        response = self.app.post(
            '/api/v1/login', content_type="application/json", data=json.dumps(self.userlogin))
        self.assertEqual(response.json, {"msg": "You are logged in as daniel"})
        self.assertEqual(response.status_code, 200)

    def test_posting_a_qn(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn1))
        self.assertEqual(
            response.json, {"msg": "your question has been added"})
        self.assertEqual(response.status_code, 201)

    def test_posting_a_qn_missing_field(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn2))
        self.assertEqual(
            response.json, {"error": "You have missed out some info, check the keys too"})
        self.assertEqual(response.status_code, 400)

    def test_qnid_taken_already(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn3))
        self.assertEqual(
            response.json, {"msg": "This qn id has been already used. Choose another integer value"})
        self.assertEqual(response.status_code, 400)
    
    def test_user_posting_not_signed_up(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn4))
        self.assertEqual(
            response.json, {"msg": "Signup to post a question"})
        self.assertEqual(response.status_code, 400)

    def test_get_all_question(self):        
        response = self.app.get('/api/v1/questions', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_qn_by_id(self):
        response = self.app.get('/api/v1/questions/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_answer_to_non_existing_qn_id(self):
        response = self.app.post(
            '/api/v1/20/ans', content_type="application/json", data=json.dumps(self.answer))
        self.assertEqual(
            response.json, {"msg": "question doesnt exist"})
        self.assertEqual(response.status_code, 404)

    def test_answer_with_taken_id(self):
        response = self.app.post(
            '/api/v1/1/ans', content_type="application/json", data=json.dumps(self.answer))
        self.assertEqual(
            response.json, {"msg": "This answer id has been already used. Choose another integer value"})
        self.assertEqual(response.status_code, 400)

    def test_answer_successfully(self):
        response = self.app.post(
            '/api/v1/1/ans', content_type="application/json", data=json.dumps(self.answer2))
        self.assertEqual(response.status_code, 200)

    def test_get_all_answers(self):
        response = self.app.get(
            '/api/v1/answers', content_type="application/json")
        self.assertEqual(response.status_code, 200)
        
        
        
        
             
