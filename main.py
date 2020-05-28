from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers,GetByMonthControlers , HomePage
from Services import DbServices
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

DbServices.CreateTables()

api.add_resource(HomePage.HomePage, '/')
api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddSimple')
api.add_resource(AddCredCardControlers.AddCredCard, '/AddCard')
api.add_resource(AddValuesCardControlers.AddValuesCredCard, '/AddValuesCard')

# get

api.add_resource(GetByMonthControlers.GetDebtsByMonth, '/GetValuesByMOnth/<Month>/<Year>')

if __name__ == '__main__':
    app.run(debug=True)