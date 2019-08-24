from flask import request
from flask_restful import Resource
import time
import json


class Search(Resource):
    def get(self, keyword):
        data = {'status': 'OK'}
        return data, 200

class Add(Resource):
    def post(self):
        mydata = request.json
        data = {'status': 'OK'}
        return data, 200

class Delete(Resource):
    def delete(self, id):
        data = {'status': 'OK'}
        return data, 200
