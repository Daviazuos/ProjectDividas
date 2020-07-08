from flask_restful import Resource
from Services import DbServices

class GetCards(Resource):
    def get(self):
        return DbServices.GetCards()

class GetCardsNames(Resource):
    def get(self):
        return DbServices.GetCardsNames()

class GetDebtsSum(Resource):
    def get(self, Month,Year):
        return DbServices.GetDebtsSum(Month, Year)

class GetCardsSum(Resource):
    def get(self, Month,Year):
        return DbServices.GetCardsSum(Month, Year)

class GetAllDebtsSum(Resource):
    def get(self, Month,Year):
        return DbServices.GetAllDebtsSum(Month, Year)

class GetAllSum(Resource):
    def get(self, Year):
        return DbServices.GetAllDebtsByMonth(Year)

class GetMonthDebtsSum(Resource):
    def get(self, Year):
        return DbServices.GetAllDebtsByMonth(Year)[0]

class GetMonthCardsSum(Resource):
    def get(self, Year):
        return DbServices.GetAllDebtsByMonth(Year)[1]
