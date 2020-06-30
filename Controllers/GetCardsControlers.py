from flask_restful import Resource
from Services import DbServices

class GetCards(Resource):
    def get(self):
        return DbServices.GetCards()

class GetCardsNames(Resource):
    def get(self):
        return DbServices.GetCardsNames()