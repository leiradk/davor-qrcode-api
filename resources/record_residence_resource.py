"""Do something Here!"""
from flask_restful import Resource, request
from flask import jsonify
import os
import json

class AddNewResidence(Resource):
    def put(self):
        jsn = {}
        data = request.data
        data = json.loads(data)
        
        token = data.get('token')
        username = data.get('username')
        action = data.get('action')

        # res = json.dumps(addToArchiveUserFunction(token, username, action))
        # res = json.loads(res)
        # res = res[0]

        # jsn = {"status": res.get('status'), "message": res.get('message')}, res.get('status')
        jsn = {}
 
        return jsn
        