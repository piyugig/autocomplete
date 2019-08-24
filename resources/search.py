from flask import request, current_app
from flask_restful import Resource
import time
import json
from redisearch import TextField, NumericField, Query, AutoCompleter, Suggestion


class Search(Resource):
    def get(self):
        keyword = request.args['term']
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.get_suggestions(keyword, fuzzy = True)
        return {"suggestion": [x.string for x in res]}, 200

class Add(Resource):
    def post(self):
        mydata = request.json
        location = str(mydata['location'])
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.add_suggestions(Suggestion(location, 1.0), increment = False)
        data = {'msg': res}
        return data, 200

class Delete(Resource):
    def post(self):
        mydata = request.json
        location = str(mydata['location'])
        ac = AutoCompleter(current_app.config["REDISSEARCH_INDEX"], current_app.config["REDISSEARCH_URI"])
        res = ac.delete(location);
        if res == 1:
            data = {'msg': 'Location deleted'}
        else:
            data = {'msg': 'Location not found'}
        return data, 200
