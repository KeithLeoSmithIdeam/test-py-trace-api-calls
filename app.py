#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from urllib import request
import logging

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req = request
    #body = request.get_json()
    #print(body)
    #url = req.url
    #print(url)
    return 'You want path: %s' % path

# @app.route('/')
# def index():
#     return json.dumps({'name': 'alice',
#                        'email': 'alice@outlook.com'})

app.run()