from views import app, api, SubscriberCollection, SubscriberLogin, QuestionCollection, SingleQnCollection


api.add_resource(SubscriberCollection, '/subscribers')
api.add_resource(SubscriberLogin, '/login')
api.add_resource(QuestionCollection, '/questions')
api.add_resource(SingleQnCollection, '/questions/<int:qn_id>')

if __name__ == '__main__':
    app.run(debug=True)
