from flask import Flask, render_template
from flask_restful import Resource, Api
from resources import search
from flask_rq2 import RQ
from flasgger import Swagger
import os
from pipelines.queue import rq

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile(os.path.join("config", 'settings.py'))
swagger = Swagger(app)

# Initiate Queue
rq.init_app(app)
api.add_resource(search.Search, '/query')
api.add_resource(search.Add, '/add')
api.add_resource(search.Delete, '/delete')

if __name__ == '__main__':
    app.run(
        host=app.config["HOST"], port=app.config["PORT"],
        debug=app.config["DEBUG"], load_dotenv=False
    )
