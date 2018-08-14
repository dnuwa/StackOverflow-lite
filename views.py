from flask import Flask, request
from flask_restful import Resource, Api
from models import User


app = Flask(__name__)
api = Api(app)

# users = [
#     {'display_name':'daniel','email': 'daniel@gmail.com','password':'1234', 'id':1 }
# ]

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

class QuestionCollection(Resource):
    def post(self):
        return {'msg':'will create a qn'}

    def get(self):
        return {'msg':'All questions'} 

class SingleQnCollection(Resource):
    def get(self, qn_id):
        return {'msg':'Queried Qn'}

class AnswerCollection(Resource):
    def post(self, qn_id):
        return {'msg':'post and answer'}