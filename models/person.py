import psycopg2

class Person:
	def __init__(self, called, givenName=None,
				 surName=None, maidenName=None,
				 birthDate=None, gender=None,
				 hasUserAccount=False, isTeamMember=False, id=None):
		self.called = called
		self.givenName = givenName
		self.surName = surName
		self.maidenName = maidenName
		self.birthDate = birthDate
		self.gender = gender
		self.hasUserAccount = hasUserAccount
		self.isTeamMember = isTeamMember


#the below code is an attempt to get scripting working with Postgres
def save_to_db(self):
	connection = psycopg2.connect(user='postgres', database='snapshot_dev', host='localhost')
	with connection.cursor as cursor:
		cursor.execute('INSERT INTO persons (called, givenName, surName, maidenName, birthDate, gender, hasUserAccount, isTeamMember) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
			(self.called, self.givenName, self.surName, self.maidenName, self.birthDate, self.gender, self.hasUserAccount, self.isTeamMember))
	
	connection.commit()
	connection.close()