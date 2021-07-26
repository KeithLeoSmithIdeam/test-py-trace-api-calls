import json
from flask import Flask, request
import logging

app = Flask(__name__)

class Stats:
    def __init__(self, url, data, method,headers, args):
      self.url = url
      self.data = data
      self.method = method
      self.headers = headers
      self.args = args
    def print(self):
        str = (
        f"URL: \t {self.url} \n"
        f"METHOD \t {self.method} \n"
        f"HEADERS \t {self.headers} \n"
        f"ARGS \t {self.args} \n"
        f"DATA: \t {self.data} \n\n"
        )
        print(str)


@app.route('/',methods = ['GET','POST','PUT', 'PATCH'], defaults={'path': ''})
@app.route('/<path:path>',methods = ['GET','POST','PUT', 'PATCH'])
def catch_all(path):
    req = request
    req_data = request.get_json()
    url = request.base_url
    headers = request.headers
    method = request.method
    args = request.args
    stats = Stats(url,req_data,method,headers,args)
    stats.print()
    return ""

# @app.route('/')
# def index():
#     return json.dumps({'name': 'alice',
#                        'email': 'alice@outlook.com'})

app.run()