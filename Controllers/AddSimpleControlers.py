from flask_restful import Resource, reqparse
from Models import Models
from Services import SendDbServices
from Services import ConnectionServices

parser = reqparse.RequestParser()

parser.add_argument('Name', type=str)
parser.add_argument('Valor', type=float)
parser.add_argument('Vencimento', type=str)
parser.add_argument('QuantidadeParcelas', type=str)
parser.add_argument('TipoDeDivida', type=str)

connection = ConnectionServices.conn().ConnPostgres()

class AddSimpleDebts(Resource):
    def post(self):
        # adicionando dívidas simples
        args = parser.parse_args()
        DebtsValues, uniqueId = Models.AddDebtsValuesModels(args)
        AddValues = SendDbServices.SendSimpleDebts(connection,DebtsValues[uniqueId])
        if AddValues:
            return uniqueId,200
        else:
            return 400
    def get(self):
        return "Hello World"