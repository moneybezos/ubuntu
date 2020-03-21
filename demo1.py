from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():

    # get x,y from the posted data
    dataDict = request.get_json()
    # return jsonify(dataDict)
    x = dataDict["x"]
    y= dataDict["y"]
    # if "y" not in dataDict:
    #     return "ERROR", 305

    # add z=x+y
    z=x+y
    #prepare a Jason "z":z
    retJSON12 = {
    "z":z
    }
    # return jsonify(map_prepared)
    return jsonify(retJSON12)



@app.route('/bye')
def bye():
    age = 4**3
    retrJson1={
    'test1':123
    }
    retJson={
    'array':[1,2,4,5,'bro'],
    # {
    # 'test1':true
    # },
    'name': 'oci baba',
    'age' : age,
    "phones":[
    {
    "phoneModel":'Oneplus',
    "phoneNumber":'2016586593'
    },
    {
    "phoneNumber":"1231231231",
    "phoneModel":"Samsung 32"
    }
    ]

    }
    # jsonify(retJson),
    return  jsonify(retJson)
    # c=2*4
    # s=str(c)
    # return "bye"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

if __name__=="__main__":
    app.run(host="127.0.0.1",port=80)
