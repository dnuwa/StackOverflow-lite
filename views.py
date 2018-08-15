from flask import Flask, request
from flask_restful import Resource, Api
from models import User, Qn, Answer


app = Flask(__name__)
api = Api(app)


def get_qn_by_id(qn_id):
    for qn in Qn.questions:
        if qn.get('qn_id') == int(qn_id):
            return qn


class SubscriberCollection(Resource):

    def post(self):
        data = request.get_json()
        id = data['id']
        display_name = data['display_name']
        password = data['password']
        # hashed_password = generate_password_hash(
        #     data['password'], method='sha256')
        email = data['email']
        new_user = User()
        new_user.signup(display_name, email, password, id)
        return {'message': 'A new user has been added'}, 201

    def get(self):
        data = User.users
        return {'registered users': data}, 200


class SubscriberLogin(Resource):
    def post(self):

        data = request.get_json()
        name = data['display_name']
        password = data['password']

        for user in User.users:
            if user['display_name'] == name and user['password'] == password:
                return {'message': 'You are logged in'}, 200
            else:
                return {'msg': 'Your username or password is incorrect'}, 401


class QuestionCollection(Resource):
    def post(self):
        data = request.get_json()
        qn_id = data['qn_id']
        qn = data['qn']
        name = data['display_name']
        new_qn = Qn()
        new_qn.add_qn(name, qn_id, qn)
        return {'msg': 'your question has been added'}, 201

    def get(self):
        All_Qns = Qn()
        return {'All Questions': All_Qns.questions}, 200


class SingleQnCollection(Resource):
    def get(self, qn_id):
        question = get_qn_by_id(qn_id)
        if not question:
            return {'msg': 'question doesnt exist'}, 404

        return question, 200


class AnswerCollection(Resource):
    def post(self, qn_id):
        data = request.get_json()
        question = get_qn_by_id(qn_id)
        if not question:
            return {'msg': 'question doesnt exist'}, 404

        for qn_id in question:
            qn = question['qn']
        ans_id = data['ans_id']
        ans = data['ans']

        new_answer = Answer()
        new_answer.add_an_answer(ans_id, qn, ans)
        return Answer.answers, 200