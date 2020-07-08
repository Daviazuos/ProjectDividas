from flask_restful import Resource
from Services import DbServices

class GetDebtsByMonth(Resource):
    def get(self, Month,Year):
        return DbServices.GetValuesByMonth(Month,Year)

class GetSimpleDebtsByCurrentMonth(Resource):
    def get(self):
        return DbServices.GetValuesByCurrentMonth()

class GetCardDebtsByCurrentMonth(Resource):
    def get(self):
        return DbServices.GetCardValuesByCurrentMonth()
