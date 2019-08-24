from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'microservice': 'Location Search'}

api.add_resource(HelloWorld, '/')

@app.route("/search")
def login():
  return render_template('index.html')

@app.route("/query")
def login():
  return render_template('index.html')

@app.route("/add")
def login():
  return render_template('index.html')

@app.route("/delete")
def login():
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')