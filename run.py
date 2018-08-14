from views import app, api, SubscriberCollection



api.add_resource(SubscriberCollection, '/subscribers')

if __name__ == '__main__':
    app.run(debug = True)