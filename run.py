from views import app, api, SubscriberCollection, SubscriberLogin


api.add_resource(SubscriberCollection, '/subscribers')
api.add_resource(SubscriberLogin, '/Login')

if __name__ == '__main__':
    app.run(debug=True)
