from flask import request
from flask_restful import Resource
import time
import json
from redisearch import TextField, NumericField, Query, AutoCompleter, Suggestion


class Search(Resource):
    def get(self, keyword):
        ac = AutoCompleter('ac', 'redis-search')
        ac.add_suggestions(
            Suggestion('google', 5.0),
            Suggestion('goo', 1.0)
        )
        res = ac.get_suggestions('goo')
        res = ac.get_suggestions('goo', fuzzy = True)
        return res, 200

class Add(Resource):
    def post(self):
        mydata = request.json
        data = {'status': 'OK'}
        return data, 200

class Delete(Resource):
    def delete(self, id):
        data = {'status': 'OK'}
        return data, 200
