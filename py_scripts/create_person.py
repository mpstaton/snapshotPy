
from models.person import Person

newPerson = Person(called="Don", givenName="Donald", surName="Burton", gender="Male", hasUserAccount=True, isTeamMember=True)

newPerson.addToDB()
