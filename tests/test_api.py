import unittest
import json
from app.views import api, app
from app.models import Qn, Answer
from run import api


class TestStackOverFlowliteApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        self.qn1 = {
            "qn_id": 2,
            "qn": "is a string a data type?",
            "display_name": "daniel"
        }
        self.qn2 = {"qn_id": "5", "qn": "is a string a data type?",
                    "display_name": "daniel"}

        self.qn3 = {'display_name': 'daniel',
                    'qn_id': 1, 'qn': 'what is a datastructure'}
        self.qn4 = {'display_name': 'johnie', 'qn_id': 4,
                    'qn': 'what is a computer science'}

        self.answer = {"ans_id": 1, "ans": "dictionaries"}
        self.answer2 = {"ans_id": 2, "ans": "some_text"}
        self.answer3 = {"ans": "some_text"}
        self.answer4 = {"ans_id": 3, "ans": "some_text"}

    def test_unsubscribed_user_attempts_adding_a_qn(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn1))
        self.assertEqual(
            response.json, {'msg': 'Signup to post a question'})

    def test_posting_a_qn_missing_field(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn2))
        self.assertEqual(response.status_code, 400)

    def test_user_posting_not_signed_up(self):
        response = self.app.post(
            '/api/v1/questions', content_type="application/json", data=json.dumps(self.qn4))
        self.assertEqual(
            response.json, {"msg": "Signup to post a question"})
        self.assertEqual(response.status_code, 400)

    def test_get_all_question(self):
        response = self.app.get('/api/v1/questions',
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_answer_to_non_existing_qn_id(self):
        response = self.app.post(
            '/api/v1/questions/20/answers', content_type="application/json", data=json.dumps(self.answer))
        self.assertEqual(response.status_code, 400)

    def test_get_all_answers(self):
        response = self.app.get(
            '/api/v1/answers', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_answer_with_empty_field(self):
        response = self.app.post(
            '/api/v1/questions/1/answers', content_type="application/json", data=json.dumps(self.answer3))
        self.assertEqual(response.status_code, 400)
        self.assertRaises(ValueError)
