from models.collectedDataPoint import CollectedDataPoint
from models.contactCard import ContactCard
from models.interaction import Interaction
from models.interactionMaterial import InteractionMaterial
from models.organization import Organization
from models.person import Person
from models.variableDocumentation import VariableDocumentation
import uuid


def getStrInput(param):
    value = input(param + ": ")
    if value == "nil":
        return None
    else :
        return value;


def getStrArrInput(param):
    value = input(param + " (seperated by,): ")
    if value == "nil":
        return None
    else :
        return [str(a) for a in value.split()]


def createOrganization(organization):
    organization = Organization();
    print("Enter details of the organization: called, long name, legal name, uri, emailSuffix, classifiers")
    print("Enter nil if not present.")
    organization.called = getStrInput("Called")
    organization.longName = getStrInput("Long name")
    organization.legalName = getStrInput("Legal name")
    organization.uri = getStrInput("Uri")
    organization.emailSuffix = getStrInput("Email Suffix")
    organization.classifiers = getStrArrInput("Classifiers")

def findOrganizationUUID():
    orgCalled = input("Search for the organization you interacted with: ")
    organizationResults = Organization.findByCalled(orgCalled)
    if len(organizationResults) == 0:
        print(orgCalled + " is not in the database, please add it to the database")
        return createOrganization(orgCalled).uuid
    else:
        print("Here are the organizations found: ")
        for i in range(0, len(organizationResults)):
            print("    " + str(i+1) + ". " + organizationResults[i].called)
        i = input("Type the index of the organization you interacted with: ")
        return organizationResults[i-1].uuid


def addInteractionStepByStep():
    print("Follow the steps below to add an interaction.")
    #interaction = Interaction()
    organizationUUID = findOrganizationUUID()
    print(organizationUUID)



addInteractionStepByStep()