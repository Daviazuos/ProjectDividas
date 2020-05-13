from flask import Flask
from flask_restful import Api
from Controllers import AddSimpleControlers
from Services import ConnectionServices

app = Flask(__name__)
api = Api(app)

api.add_resource(AddSimpleControlers.AddSimpleDebts, '/AddSimple')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
