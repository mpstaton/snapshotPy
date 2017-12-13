
from models.organization import Organization

newOrg = Organization(called="testOrg", longName="test organization")

newOrg.addToDB()
