from flask_restful import Resource
from Services import DbGetServices

class GetReceived(Resource):
    def get(self):
        return DbGetServices.GetReceived()

class GetSumReceived(Resource):
    def get(self):
        return DbGetServices.GetSumReceived()