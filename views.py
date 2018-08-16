from flask import Flask, request
from flask_restful import Resource, Api
from models import User, Qn, Answer


app = Flask(__name__)
api = Api(app, prefix="/api/v1")


def get_qn_by_id(qn_id):
    for qn in Qn.questions:
        if qn.get('qn_id') == int(qn_id):
            return qn


class SubscriberCollection(Resource):

    def post(self):
        data = request.get_json()
        if (not data or
            "password" not in data or
            "display_name" not in data or
                "email" not in data):
            return {"error": "You have missed out some info, check the keys too"}, 400

        display_name = data['display_name']
        password = data['password']
        email = data['email']

        for user in User.users:
            if user['display_name'] == display_name or user['email'] == email:
                return {'msg': 'This account already exists'}, 400
        else:

            new_user = User()
            new_user.signup(display_name, email, password)
            return {'msg': 'you have signed up as {}'.format(display_name)}, 201

    def get(self):
        data = User.users
        return {'registered users': data}, 200


class SubscriberLogin(Resource):
    def post(self):

        data = request.get_json()
        if (not data or
            "password" not in data or
                "display_name" not in data):
            return {"error": "You have missed out some info, check the keys too"}, 400

        name = data['display_name']
        password = data['password']

        for user in User.users:

            if user['display_name'] == name and user['password'] == password:
                return {'msg': 'You are logged in as {}'.format(name)}, 200

        else:
            return {'msg': 'Your username or password is incorrect'}, 401


class QuestionCollection(Resource):
    def post(self):
        data = request.get_json()
        if (not data or
            "qn_id" not in data or
                "qn" not in data or
                "display_name" not in data):
            return {"error": "You have missed out some info, check the keys too"}, 400

        query_id = data['qn_id']
        qn = data['qn']
        name = data['display_name']

        for user in User.users:
            if user['display_name'] == name:
                for query in Qn.questions:
                    if query['qn_id'] == query_id:
                        return {'msg': 'This qn id has been already used. Choose another integer value'}, 400

                new_qn = Qn()
                new_qn.add_qn(name, query_id, qn)
                return {'msg': 'your question has been added'}, 201

        return {'msg': 'Signup to post a question'}, 400

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
        answer_id = data['ans_id']
        ans = data['ans']

        for answer in Answer.answers:
            if answer['ans_id'] == answer_id:
                return {'msg': 'This answer id has been already used. Choose another integer value'}, 400

        new_answer = Answer()
        new_answer.add_an_answer(answer_id, qn, ans)
        return Answer.answers, 200

    # def get(self, qn_id):
    #     All_answers = Answer()
    #     answers =All_answers.answers
    #     question = get_qn_by_id(qn_id)
    #     if not question:
    #         return {'msg': 'question doesnt exist'}, 404

    #     for qn_id in question:
    #         for ans in answers:
    #             return All_answers.answers, 200


class AnswersToAll(Resource):
    def get(self):
        All_answers = Answer()
        return All_answers.answers, 200
