from flask_restful import Resource, reqparse
from Models import Models
from Services import DbServices

parser = reqparse.RequestParser()

class AddValuesCredCard(Resource):
    def post(self):
        parser.add_argument('CardName', type=str)
        parser.add_argument('Valor', type=float)
        parser.add_argument('QuantidadeDeParcelasCartao', type=int)
        parser.add_argument('TipoDeDividaCartao', type=str)
        parser.add_argument('DataCompra', type=str)
        parser.add_argument('Descricao', type=str)

        # adicionando valores ao cartão de crédito

        args = parser.parse_args()
        DebtsValues, uniqueId = Models.AddValuesCredCard(args)
        AddValues = DbServices.SendValuesCredCard(DebtsValues)
        if AddValues:
            return uniqueId,200
        else:
            return 400

    def get(self):
        return {
            "CardName": "Nubank",
            "Valor": 150.00,
            "QuantidadeDeParcelas": 10,
            "TipoDeDivida": "Parcelada",
            "DataCompra": "2020-05-15",
            "Descricao": "Livros"
        }