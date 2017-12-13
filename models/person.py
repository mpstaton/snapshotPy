from database import connect

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

    # the below code is an attempt to get scripting working with Postgres
    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO persons (id, called, givenName, surName, maidenName, birthDate, gender, hasUserAccount, '
                    'isTeamMember) VALUES (1, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.called, self.givenName, self.surName, self.maidenName, self.birthDate, self.gender,
                     self.hasUserAccount, self.isTeamMember))
            # conn.commit()
            # conn.close()

person1 = Person(called="testperson", givenName="givenname", surName="surname", gender="Male", hasUserAccount="True", isTeamMember="True")
person1.addToDB()