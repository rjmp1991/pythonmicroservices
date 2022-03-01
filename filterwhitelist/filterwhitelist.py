
from flask import Flask
from flask_restful import Api
import requests, concurrent.futures

app = Flask(__name__)
api = Api(app)


def worker(url):
    response = requests.request("GET", url)
    return response.text

#default path
@app.route('/', methods=['GET'])
def default():
    return "filterwhitelist works!!!", 200

#getInfo path
@app.route('/filterwhitelist', methods=['GET'])
def filter():

    try:
        executor = concurrent.futures.ThreadPoolExecutor()
        iplist = executor.submit(worker,"http://localhost:8080/getips")
        whitelist = executor.submit(worker,"http://localhost:8082/getwhitelist")
 
        wList = whitelist.result().split(',')
        torList = iplist.result().split('\n')
        filter=""

        for itemtor in torList:
            flag=True
            for w in wList:
                if(itemtor==w):
                    print("ip descartada : "+w)
                    flag=False
            if(flag):
                filter+=itemtor+"\n"    


    except:
        return "error ", 503

    return filter, 200


#Error path
@app.errorhandler(404)
def page_not_found(e):
    return "Path not found", 404

#start
if __name__ == '__main__':
    app.run(port='8083', host='0.0.0.0')