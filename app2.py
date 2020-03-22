from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData,functionName):
    if (functionName == 'add1'):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200


class Add1(Resource):
    def add1(self):
        postedData = request.get_json()
        status = checkPostedData(postedData, "add1")
        if status!=200:
            retJson={
            "message":"a message has occured",
            "status": status
            }
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        z = x + y
        reqMap = {
            "Sum": z,
            "Message": 200
            }
        return reqMap



api.add_resource(Add1, '/add1')

if __name__=="__main__":
    app.run()
