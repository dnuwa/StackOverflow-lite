class User:
    users = [
        {'display_name': 'daniel', 'email': 'daniel@gmail.com', 'password': '1234', 'id': 1}, {
            'display_name': 'jose', 'email': 'daniel@gmail.com', 'password': '1234', 'id': 2}
    ]
    
    def __init__(self):
        self.new_user = {}

    def signup(self, display_name, email, password, id):
        self.new_user['display_name'] = display_name
        self.new_user['email'] = email
        self.new_user['password'] = password
        self.new_user['id'] = id
        self.users.append(self.new_user)


class Qn:
    questions = [
        {'qn_id': 1, 'qn': 'what is a datastructure', 'display_name': 'daniel'}]

    def __init__(self):
        self.question = {}

    def add_qn(self, name, qn_id, qn ):
        self.question['qn_id'] = int(qn_id)
        self.question['qn'] = qn
        self.question['name'] = name
        self.questions.append(self.question)