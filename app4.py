from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkP_data(pData, funcName):
    if funcName=="add4":
        if "x" not in pData or "y" not in pData:
            return 304
        else:
            return 200


class Add4(Resource):
    def post(self):
        pData = request.get_json()
        resultChek = checkP_data(pData, "add4")
        if resultChek!=200:
            retResChecl = {
            "Message Fail Dawg": "Failed My Man",
            "Status Code":resultChek
            }
            return retResChecl
        x = pData['x']
        y = pData['y']
        x=int(x)
        y=int(y)
        retZ = x + y
        retJZ = {
        "Message Good":retZ,
        "Status Code":200
        }
        return jsonify(retJZ)
#{"Message Good": 246, "Status Code": 200}
api.add_resource(Add4, '/add4')

if __name__=="__main__":
    app.run(debug=True)
