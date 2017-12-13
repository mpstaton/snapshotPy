
from models.person import Person

person1 = Person(called="Don", givenName="Donald", surName="Burton", gender="Male", hasUserAccount=True, isTeamMember=True)

person1.addToDB()
