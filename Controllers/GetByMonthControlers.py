from flask_restful import Resource
from Services import DbGetServices

class GetSimpleDebtsByCurrentMonth(Resource):
    def get(self):
        return DbGetServices.GetValuesByCurrentMonth()

class GetCardDebtsByCurrentMonth(Resource):
    def get(self):
        return DbGetServices.GetCardValuesByCurrentMonth()