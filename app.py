from flask import Flask
from flask_restful import Resource, Api
import helloJSON

app = Flask(__name__)
app.debug = True
api = Api(app)

class HelloWorld(Resource):
	def get(self, api_key):
		data = helloJSON.getJSON(api_key)
		print(data)

		return {'Hello': 'World'}

api.add_resource(HelloWorld, '/<string:api_key>')

if __name__ == '__main__':
    app.run()