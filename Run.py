from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers

app = Flask(__name__)
api = Api(app)

api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddSimple')
api.add_resource(AddCredCardControlers.AddCredCard, '/AddCard')
api.add_resource(AddValuesCardControlers.AddValuesCredCard, '/AddValuesCard')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')