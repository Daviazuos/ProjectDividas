from flask_restful import Resource
from Services import DbGetServices

class GetCards(Resource):
    def get(self):
        return DbGetServices.GetCards()

class GetCardsNames(Resource):
    def get(self):
        return DbGetServices.GetCardsNames()

class GetDebtsSum(Resource):
    def get(self, Month,Year):
        return DbGetServices.GetDebtsSum(Month, Year)

class GetCardsSum(Resource):
    def get(self, Month,Year):
        return DbGetServices.GetCardsSum(Month, Year)

class GetAllDebtsSum(Resource):
    def get(self, Month,Year):
        return DbGetServices.GetAllDebtsSum(Month, Year)

class GetMonthSum(Resource):
    def get(self, Year):
        return DbGetServices.GetAllDebtsByMonth(Year)

class GetMonthCardsSum(Resource):
    def get(self, Year):
        return DbGetServices.GetAllDebtsByMonth(Year)[1]
