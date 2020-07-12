from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers,GetByMonthControlers , GetCardsControlers, HomePage
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# post

# Adicionando Cartao de Credito
api.add_resource(AddCredCardControlers.AddCredCard, '/AddCard')

# Adicionando Dividas ou valores ao Cartao de Credito
api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddDebts')
api.add_resource(AddValuesCardControlers.AddValuesCredCard, '/AddValuesCard')

# get

api.add_resource(HomePage.HomePage, '/')

# Get all values (card and simple) by current month
api.add_resource(GetByMonthControlers.GetSimpleDebtsByCurrentMonth, '/Simple')
api.add_resource(GetByMonthControlers.GetCardDebtsByCurrentMonth, '/Card')

# Get values from cards
api.add_resource(GetCardsControlers.GetCards, '/GetCards')
api.add_resource(GetCardsControlers.GetCardsNames, '/GetCardsNames')

# Sums

api.add_resource(GetCardsControlers.GetDebtsSum, '/GetDebtsSum/<Month>/<Year>')
api.add_resource(GetCardsControlers.GetCardsSum, '/GetCardsSum/<Month>/<Year>')

api.add_resource(GetCardsControlers.GetAllDebtsSum, '/GetAllDebtsSum/<Month>/<Year>')

api.add_resource(GetCardsControlers.GetMonthSum, '/GetMonthSum/<Year>')

if __name__ == '__main__':
    app.run(debug=True)