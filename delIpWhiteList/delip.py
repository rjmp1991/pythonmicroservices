from flask import Flask
from flask_restful import Api
from flask import request
import json, re

app = Flask(__name__)
api = Api(app)


#default path
@app.route('/', methods=['DELETE'])
def default():
    return "delip works!!!", 200

#getInfo path
@app.route('/delip', methods=['DELETE'])
def delIp():
    regexv4 = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    regexv6 = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
    try:
        if request.data != b'':
            if( 'ip' in json.loads(request.data)):
                ip = json.loads(request.data)['ip']
                if re.search(regexv4, ip) or re.search(regexv6, ip):
                   
                    #incluir el código para eliminar la ip de la lista blanca
                    return "Deleted ip: "+ip , 200
                else:
                    return "You must send a valid ip " + ip, 200
            else:
                return "You did not send ip in data request", 200
        else:
            return "You did not send data", 200
    except:
        return "Error check logs!!!", 503 

#Error path
@app.errorhandler(404)
def page_not_found(e):
    return "Path not found", 404

#start
if __name__ == '__main__':
    app.run(port='8084', host='0.0.0.0')