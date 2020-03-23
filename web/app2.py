from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
def checkPostedData(postedData,functionName):
    if (functionName == 'add1'):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    if (functionName == 'subtract1'):
        if "x" not in postedData or "y" not in postedData:
            return 302
        else:
            return 200
    if (functionName == 'multiply1'):
        if "x" not in postedData or "y" not in postedData:
            return 303
        else:
            return 200
    if (functionName == 'divide1'):
        if postedData["y"]==0:
            return 404
        elif "x" not in postedData or "y" not in postedData:
            return 304
        else:
            return 200

class Divide1(Resource):
    def post(self):
        postedData = request.get_json()
        status = checkPostedData(postedData, "divide1")
        if (status!=200):
            retJson={
            "message bro":"a message has occured",
            "status": status
            }
            return jsonify(retJson)
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = (x*1.0)  / y
        retMap = {
            'Divide': ret,
            'Message': 200
            }
        return jsonify(retMap)
class Multiply1(Resource):
    def post(self):
        postedData = request.get_json()
        status = checkPostedData(postedData, "multiply1")
        if (status!=200):
            retJson={
            "message bro":"a message has occured",
            "status": status
            }
            return jsonify(retJson)
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            'Multiply': ret,
            'Message': 200
            }
        return jsonify(retMap)

class Add1(Resource):
    def post(self):
        postedData = request.get_json()
        status = checkPostedData(postedData, "add1")
        if (status!=200):
            retJson={
            "message bro":"a message has occured",
            "status": status
            }
            return jsonify(retJson)
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x + y
        retMap = {
            'Sum': ret,
            'Message': 200
            }
        return jsonify(retMap)

class Subtract1(Resource):
    def post(self):
        postedData = request.get_json()
        status = checkPostedData(postedData, "subtract1")
        if (status!=200):
            retJson={
            "message bro":"a message has occured",
            "status": status
            }
            return jsonify(retJson)
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            'Subtract': ret,
            'Message': 200
            }
        return jsonify(retMap)

api.add_resource(Add1, "/add1")
api.add_resource(Subtract1, "/subtract1")
api.add_resource(Multiply1, "/multiply1")
api.add_resource(Divide1, "/divide1")


if __name__=="__main__":
    app.run(debug=True)
