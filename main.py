from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers,GetByMonthControlers , GetCardsControlers
from Services import DbServices
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

DbServices.CreateTables()

# post

api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddSimple')
api.add_resource(AddCredCardControlers.AddCredCard, '/AddCard')
api.add_resource(AddValuesCardControlers.AddValuesCredCard, '/AddValuesCard')

# get

api.add_resource(GetByMonthControlers.GetSimpleDebtsByCurrentMonth, '/Simple')
api.add_resource(GetByMonthControlers.GetCardDebtsByCurrentMonth, '/Card')
api.add_resource(GetByMonthControlers.GetDebtsByMonth, '/GetValuesByMOnth/<Month>/<Year>')
api.add_resource(GetCardsControlers.GetCards, '/GetCards')
api.add_resource(GetCardsControlers.GetCardsNames, '/GetCardsNames')

api.add_resource(GetCardsControlers.GetAllDebtsSum, '/GetAllDebtsSum/<Month>/<Year>')
api.add_resource(GetCardsControlers.GetDebtsSum, '/GetDebtsSum/<Month>/<Year>')
api.add_resource(GetCardsControlers.GetCardsSum, '/GetCardsSum/<Month>/<Year>')

if __name__ == '__main__':
    app.run(debug=True)