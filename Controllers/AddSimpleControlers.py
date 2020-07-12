from flask_restful import Resource, reqparse
from Models import Models
from Services import DbPostServices

parser = reqparse.RequestParser()

class AddSimpleDebts(Resource):
    def post(self):
        parser.add_argument('Name', type=str)
        parser.add_argument('Valor', type=float)
        parser.add_argument('Vencimento', type=str)
        parser.add_argument('QuantidadeParcelas', type=str)
        parser.add_argument('TipoDeDivida', type=str)

        # adicionando dívidas simples

        args = parser.parse_args()
        DebtsValues, uniqueId, result = Models.AddDebtsValuesModels(args)
        if result:
            AddValues = DbPostServices.SendDebtsValues(DebtsValues)
        else:
            return DebtsValues, 400
        if AddValues:
            return uniqueId,200
        else:
            return 400

    def get(self):
        return {
            "Name": "Davi",
            "Valor": 150.00,
            "Vencimento": "2020-05-15",
            "QuantidadeParcelas": 10,
            "TipoDeDivida": "Parcelada"
        }