from flask import Flask

app = Flask(__name__)

@app.route('/organizations', methods=['POST'])
	def create_organization
		#create an organization with kwargs


app.run(port=5000)