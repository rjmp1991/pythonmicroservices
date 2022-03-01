from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

#default path
@app.route('/', methods=['GET'])
def default():
    return "getwhitelist works!!!", 200

#getInfo path
@app.route('/getwhitelist', methods=['GET'])
def getList():

    try:
        #escribir el código para recuperar la lista blanca
        return '91.250.242.12,71.19.144.106,2a03:4000:0019:00e6:0000:0000:0000:0001,2a03:4000:001e:0714:8411:92ff:fe73:f0fc', 200
    except:
        return "Error check logs!!!", 503 

#Error path
@app.errorhandler(404)
def page_not_found(e):
    return "Path not found", 404

#start
if __name__ == '__main__':
    app.run(port='8082', host='0.0.0.0')