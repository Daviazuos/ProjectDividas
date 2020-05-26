from flask_restful import Resource, reqparse
from Models import Models
from Services import DbServices

parser = reqparse.RequestParser()

class AddCredCard(Resource):
    def post(self):
        parser.add_argument('CardName', type=str)
        parser.add_argument('Vencimento', type=int)
        parser.add_argument('Fechamento', type=int)

        # adicionando cartão de crédito

        args = parser.parse_args()
        DebtsValues, uniqueId = Models.AddCredCardModels(args)
        AddValues = DbServices.SendCredCard(DebtsValues)
        if AddValues:
            return uniqueId,200
        else:
            return 400

    def get(self):
        return {
            "CardName": "Nubank",
            "Vencimento": "15",
            "Fechamento": "5"
        }