from flask import Flask, jsonify, request
from flask_restful import Api, Resource
# resources give us access to HTTP methods
app = Flask(__name__)
api = Api(app)
def checkPostedData(postedData,functionName):
    if (functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
class Add(Resource):
    # @app.route('/add')
    def post(self):
        #if i am here, then resource Add was requested using post
        #step 1, get posted dataDict
        postedData = request.get_json()
        #step1b, verify validity of posted data
        status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson{
            "Message":"An error happened"
            "Status Code": status_code
            }
        x = postedData['x']
        y = postedData["y"]
        x=int(x)
        y=int(y)
        #Step 2, add posted data
        ret = x+y
        retMap = {
            # 'Message': response
            'Sum': ret,
            'Status Code': 200
        }
        return jsonify(retMap)
    # def get(self):
    #     pass
    #     #if i am here, then resource Add was requested using get
    # def put(self):
    #     pass
    #     #if i am here, then resource Add was requested using put
    # def delete(self):
    #     pass
    #     #if i am here, then resource Add was requested using delete

    pass

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add,"/add")





if __name__=="__main__":
    app.run(host="127.0.0.1",port=80)
