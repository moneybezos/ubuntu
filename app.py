from flask import Flask, jsonify, request
from flask_restful import Api, Resource

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
# @app.route('/')
# def hello_world():
#     return "Hello, World!"
#
# @app.route('/add_two_nums', methods=["POST"])
# def add_two_nums():
#
#     # get x,y from the posted data
#     dataDict = request.get_json()
#     # return jsonify(dataDict)
#     x = dataDict["x"]
#     y= dataDict["y"]
#     # if "y" not in dataDict:
#     #     return "ERROR", 305
#
#     # add z=x+y
#     z=x+y
#     #prepare a Jason "z":z
#     retJSON12 = {
#     "z":z
#     }
#     # return jsonify(map_prepared)
#     return jsonify(retJSON12)
#
#
#
# @app.route('/bye')
# def bye():
#     age = 4**3
#     retrJson1={
#     'test1':123
#     }
#     retJson={
#     'array':[1,2,4,5,'bro'],
#     # {
#     # 'test1':true
#     # },
#     'name': 'oci baba',
#     'age' : age,
#     "phones":[
#     {
#     "phoneModel":'Oneplus',
#     "phoneNumber":'2016586593'
#     },
#     {
#     "phoneNumber":"1231231231",
#     "phoneModel":"Samsung 32"
#     }
#     ]
#
#     }
#     # jsonify(retJson),
#     return  jsonify(retJson)
#     # c=2*4
#     # s=str(c)
#     # return "bye"
#
# @app.route('/hithere')
# def hi_there_everyone():
#     return "I just hit /hithere"


if __name__=="__main__":
    app.run(host="127.0.0.1",port=80)
