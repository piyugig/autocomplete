from flask import Flask, render_template
from flask_restful import Resource, Api
from resources import search

app = Flask(__name__)
api = Api(app)

api.add_resource(search.Search, '/search/<string:keyword>/')
api.add_resource(search.Add, '/search/')
api.add_resource(search.Delete, '/search/<string:id>/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
