from flask import Flask, request
from flask_restful import Resource, Api
from app.models import User, Qn, Answer
from flasgger import Swagger, swag_from
import re


app = Flask(__name__)

api = Api(app, prefix="/api/v1")

app.config['SWAGGER'] = {
    'title': 'Stackoverflow-Lite',
}
Swagger(app)


def get_qn_by_id(qn_id):
    for qn in Qn.questions:
        if qn.get('qn_id') == int(qn_id):
            return qn


class SubscriberCollection(Resource):
    
    @swag_from('add_user.yml', methods=['POST'])
    def post(self):
        user_data = request.get_json()
        try:
            display_name = user_data['display_name'].strip()
            password = user_data['password'].strip()
            email = user_data['email'].strip()

            if display_name == "" or password == "":
                return {'error': 'ensure all feilds are field correctlty'}, 400

            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return {'error': 'Invalid email address'}, 400

            for user in User.users:
                if user['display_name'] == display_name or user['email'] == email:
                    return {'msg': 'This account already exists'}, 400
                
            new_user = User()
            new_user.signup(display_name, email, password)
            return {'msg': 'you have signed up as {}'.format(display_name)}, 201

        except:
            return {"error": "You have missed out some info, check the keys too"}, 400
            
    @swag_from('swagger.yaml', methods=['GET'])
    def get(self):
        
        data = User.users
        return {'registered users': data}, 200


class SubscriberLogin(Resource):
    
    @swag_from('login.yml', methods=['POST'])
    def post(self):

        data = request.get_json()
        if (not data or
            "password" not in data or
                "display_name" not in data):
            return {"error": "You have missed out some info, check the keys too"}, 400

        name = data['display_name'].strip()
        password = data['password'].strip()

        for user in User.users:

            if user['display_name'] == name and user['password'] == password:
                return {'msg': 'You are logged in as {}'.format(name)}, 200

        else:
            return {'msg': 'Your username or password is incorrect'}, 401


class QuestionCollection(Resource):
    
    @swag_from('post_a_question.yaml', methods=['POST'])
    def post(self):
        try:

            data = request.get_json()

            query_id = data['qn_id']
            qn = data['qn'].strip()
            name = data['display_name'].strip()

            if (not isinstance(query_id, int)) and qn == "":
                return {'error': 'question field cant be empty'}, 400

            for user in User.users:
                if user['display_name'] == name:
                    for query in Qn.questions:
                        if query['qn_id'] == int(query_id):
                            return {'msg': 'This qn id has been already used. Choose another integer value'}, 400

                    new_qn = Qn()
                    new_qn.add_qn(name, query_id, qn)
                    return {'msg': 'your question has been added'}, 201

            return {'msg': 'Signup to post a question'}, 400
        
        except:
            return {"error": "You have missed out some info, check the keys too"}, 400

    @swag_from('get_all_qn.yaml', methods=['GET'])
    def get(self):        
        All_Qns = Qn()
        return {'All Questions': All_Qns.questions}, 200


class SingleQnCollection(Resource):
    
    @swag_from('get_qn_by_id.yaml', methods=['GET'])
    def get(self, qn_id):
        try:
            qn_identity = int(qn_id)

            for qn in Qn.questions:
                if qn['qn_id'] == qn_identity:
                    return qn, 200

            return {'msg': 'question doesnt exist'}, 404

        except Exception as e:
            return {'error': str(e)+",qn_id should be an integer"}, 404


class AnswerCollection(Resource):
    new_list = []

    @swag_from('post_an_answer.yaml', methods=['POST'])
    def post(self, qn_id):
        try:
            data = request.get_json()
            question = get_qn_by_id(qn_id)

            for qn_id in question:
                qn = question['qn']
                qn_identity = question['qn_id']

            answer_id = data['ans_id']
            ans = data['ans'].strip()

            if not isinstance(answer_id, int):
                return {'error': 'answer_id should be integer'}, 400

            if ans == "":
                return {'error': 'answer field cant be empty'}, 400

            for answer in Answer.answers:
                if answer['ans_id'] == answer_id:
                    return {'msg': 'This answer id has been already used. Choose another integer value'}, 400

            new_answer = Answer()
            new_answer.add_an_answer(answer_id, qn_identity, qn, ans)
            return {'msg': 'an answers has been added successfully'}, 200

        except Exception as e:
            return {'error': str(e)+', Non existing question or missing fields'}, 400

    @swag_from('qetting_answers_to_a_qn.yaml', methods=['GET'])
    def get(self, qn_id):
        self.new_list.clear()

        question = get_qn_by_id(qn_id)
        if not question:
            return {'msg': 'question doesnt exist'}, 404

        for answer in Answer.answers:
            if answer['qn_id'] == qn_id:
                self.new_list.append(answer)

        # print (self.new_list)
        return {'answers': self.new_list}, 200


class AnswersToAll(Resource):
    
    @swag_from('qetting_all_qns_and_ans.yaml', methods=['GET'])
    def get(self):
        All_answers = Answer()
        return All_answers.answers, 200
