from flask_restful import Resource, reqparse
from Models import Models
from Services import DbServices

class HomePage(Resource):
    def get(self):
        return "Hello World"