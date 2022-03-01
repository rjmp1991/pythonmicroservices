from requests_toolbelt import threaded
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

#default path
@app.route('/', methods=['GET'])
def default():
    return "getips works!!!", 200

#getInfo path
@app.route('/getips', methods=['GET'])
def getIps():
    try:
        allips=""
        urls_to_get = [{
            'url': 'https://check.torproject.org/torbulkexitlist',
            'method': 'GET',
        }, {
            'url': 'https://www.dan.me.uk/torlist/',
            'method': 'GET',
        }]
        responses, errors = threaded.map(urls_to_get)

        for response in responses:
            if(response.status_code==200):

                #Escribir código para almacenar el cache de las ips de la segunda fuente
                
                allips+=response.text             

        return allips, 200

    except:
        return "Error!!!", 200

#Error path
@app.errorhandler(404)
def page_not_found(e):
    return "Path not found", 404

#start
if __name__ == '__main__':
    app.run(port='8080', host='0.0.0.0')