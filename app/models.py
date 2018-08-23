class User:
    #{'display_name': 'daniel', 'email': 'daniel@gmail.com', 'password': '1234'}
    users = []

    def __init__(self):
        self.new_user = {}

    def signup(self, display_name, email, password):
        self.new_user['display_name'] = display_name
        self.new_user['email'] = email
        self.new_user['password'] = password

        self.users.append(self.new_user)


class Qn:
    #{'display_name': 'daniel', 'qn_id': 1, 'qn': 'what is a datastructure'}
    questions = []

    def __init__(self):
        self.question = {}

    def add_qn(self, name, qn_id, qn):
        self.question['name'] = name
        self.question['qn_id'] = int(qn_id)
        self.question['qn'] = qn

        self.questions.append(self.question)


class Answer:
    new_list = None
    #{"ans_id": 1, "qn_id":1, "qn": "what is a datastructure","ans": "dictionaries"} 
    answers = []

    def __init__(self):
        self.answer = {}

    def add_an_answer(self, ans_id, qn_id, qn, ans):

        self.answer['ans_id'] = int(ans_id)
        self.answer['qn_id'] = qn_id
        self.answer['qn'] = qn
        self.answer['ans'] = ans
        self.answers.append(self.answer)
