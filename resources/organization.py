organizations = []

class Organization(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(required=True)

	def get(self, called, longName, legalName, uri, emailSuffix, dateRegistered):
		organization = next(filter(lambda x: x['called'] == called, organizations), None)
		return {'organization': organization}, 200 if organization else 404

	def post(self, called, longName, legalName, uri, emailSuffix, dateRegistered):
		data = request.get_json(force=True)
		data = Organization.parser.parse_args()
		organization = {'called': data['called']}
		organizations.append(organization)
		return organization, 201

	def put(self, called):
		data = Organization.parser.parse_args()
		organization.update(data)
		return organization

	def delete(self):
		return {'message': 'Organization deleted'}

class OrganizationList(Resource):
	def get(self):
		return {'organizations': items}

api.add_resource(Organization, '/organization/<string:name>')
api.add_resource(OrganizationList, '/organizations')