from flask_restful import Resource
from Services import DbServices

class GetDebtsByMonth(Resource):
    def get(self, Month,Year):
        return DbServices.GetValuesByMonth(Month,Year)