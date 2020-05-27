from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers, HomePage
from Services import DbServices

app = Flask(__name__)
api = Api(app)

DbServices.CreateTables()

api.add_resource(HomePage.HomePage, '/')
api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddSimple')
api.add_resource(AddCredCardControlers.AddCredCard, '/AddCard')
api.add_resource(AddValuesCardControlers.AddValuesCredCard, '/AddValuesCard')

if __name__ == '__main__':
    app.run(debug=True)
