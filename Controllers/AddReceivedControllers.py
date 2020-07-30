from flask_restful import Resource, reqparse
from Models import Models
from Services import DbPostServices

parser = reqparse.RequestParser()

class AddReceived(Resource):
    def post(self):
        parser.add_argument('Date', type=str)
        parser.add_argument('Valor', type=float)
        parser.add_argument('Tipo', type=str)

        args = parser.parse_args()
        received, uniqueId = Models.AddReceivedModels(args)
        AddValues = DbPostServices.SendReceived(received)

        if AddValues:
            return uniqueId,200
        else:
            return 400

    def get(self):
        return {
            "Date": "05/05/2020",
            "Valor": 1500.00,
            "Tipo": "Fixa"
        }