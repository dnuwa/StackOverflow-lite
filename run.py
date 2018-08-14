from views import app, api, SubscriberCollection, SubscriberLogin, QuestionCollection


api.add_resource(SubscriberCollection, '/subscribers')
api.add_resource(SubscriberLogin, '/login')
api.add_resource(QuestionCollection, '/questions')

if __name__ == '__main__':
    app.run(debug=True)
