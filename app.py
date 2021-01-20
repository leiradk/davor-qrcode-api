"""App Server main"""
# importing dependencies or modules
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

# importing resources
from resources.record_residence_resource import AddNewResidence

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

api.add_resource(AddNewResidence, '/davor/add')

# Run the main app
if __name__ == '__main__':
    app.run(debug=True)