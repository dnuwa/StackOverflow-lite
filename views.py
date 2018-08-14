from flask import Flask, request
from flask_restful import Resource, Api
from models import User


app = Flask(__name__)
api = Api(app)


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
        return {'msg': 'will create a qn'}

    def get(self):
        return {'msg': 'All questions'}


class SingleQnCollection(Resource):
    def get(self, qn_id):
        return {'msg': 'Queried Qn'}


class AnswerCollection(Resource):
    def post(self, qn_id):
        return {'msg': 'post and answer'}
