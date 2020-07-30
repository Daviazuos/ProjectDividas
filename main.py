from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers, AddCredCardControlers, AddValuesCardControlers,GetByMonthControlers , GetCardsControlers, HomePage, AddReceivedControllers, GetReceivedControllers
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

# Adicionando valores recebidos
api.add_resource(AddReceivedControllers.AddReceived, '/AddReceived')

# get

api.add_resource(HomePage.HomePage, '/')

# Get all values (card and simple) by current month
api.add_resource(GetByMonthControlers.GetSimpleDebtsByCurrentMonth, '/Simple')
api.add_resource(GetByMonthControlers.GetCardDebtsByCurrentMonth, '/Card/<CardName>')

api.add_resource(GetReceivedControllers.GetReceived, '/GetReceived')

# Get values from cards
api.add_resource(GetCardsControlers.GetCards, '/GetCards')
api.add_resource(GetCardsControlers.GetCardsNames, '/GetCardsNames')

# Sums

api.add_resource(GetCardsControlers.GetDebtsSum, '/GetDebtsSum/<Month>/<Year>')
api.add_resource(GetCardsControlers.GetCardsSum, '/GetCardsSum/<Month>/<Year>')

api.add_resource(GetCardsControlers.GetSumByCardName, '/GetSumByCardName/<Month>/<Year>')

api.add_resource(GetCardsControlers.GetAllDebtsSum, '/GetAllDebtsSum/<Month>/<Year>')

api.add_resource(GetCardsControlers.GetMonthSum, '/GetMonthSum/<Year>')

if __name__ == '__main__':
    app.run(debug=True)