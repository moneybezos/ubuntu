from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app=Flask(__name__)
api = Api(app)


def checkSentData(postData, methodName):
    if (methodName =='add3'):
        if "x" not in postData or "y" not in postData:
            return 301
        else:
            return 200

class Add3(Resource):
    def post(self):

        postData = request.get_json()
        status = checkSentData(postData, 'add3')
        if (status!=200):
            retStat={
            "message bro ": "invalid hommie G",
            "status code":301
            }
            return retStat
        x=postData['x']
        y=postData['y']

        returnzies = x + y
        retJson={
        "message succes?": returnzies,
        "status code":200

        }


        return jsonify(retJson)

api.add_resource(Add3, '/add3')
