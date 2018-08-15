from views import app, api, SubscriberCollection, SubscriberLogin, QuestionCollection, SingleQnCollection, AnswerCollection


api.add_resource(SubscriberCollection, '/subscribers')
api.add_resource(SubscriberLogin, '/login')
api.add_resource(QuestionCollection, '/questions')
api.add_resource(SingleQnCollection, '/questions/<int:qn_id>')
api.add_resource(AnswerCollection, '/<int:qn_id>/ans')

if __name__ == '__main__':
    app.run(debug=True)
