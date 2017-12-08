from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import psycopg2

from resources.organization import Organization

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/snapshot_dev'
db = SQLAlchemy(app)

#this is Flask routing conentions without the use of 
#the restful API library. 
@app.route('/')
	def home():

@app.route('/organizations')
	def get_all_organizations():
		#get all organizations

@app.route('/organizations', methods=['POST'])
	def create_organization():
		#create an organization with kwargs

@app.route('/organization/<string:called>')
	def get_organization_by_called():
		#return a single organization object by what it is called		

#classes are implemented as a Resource object 
#to activate the Flask Restful API framework.


app.run(port=5000, debug=True)