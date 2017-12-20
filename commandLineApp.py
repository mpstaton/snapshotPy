
from models.collectedDataPoint import CollectedDataPoint
from models.contactCard import ContactCard
from models.interaction import Interaction
from models.interactionMaterial import InteractionMaterial
from models.organization import Organization
from models.person import Person
from models.variableDocumentation import VariableDocumentation
from S3Bucket import S3Bucket

def getStrInput(param):
    value = input("    " + param + ": ")
    if value == "":
        return None
    else:
        return value

def getIntInput(param):
    return int(input(param))

def getStrArrInput(param):
    value = input("    " + param + " (seperated by,): ")
    if value == "":
        return None
    else:
        return [str(a) for a in value.split()]

def getDateInput(param):
    value = input("    " + param + " (YYYYMMDD): ")
    if value == "":
        return None
    else:
        return value[:4] + "-" + value[4:6] + "-" + value[6:]

def getTimeInput(param):
    value = input("    " + param + " (HH:MM): ")
    if value == "":
        return None
    else:
        return value

def getBoolInput(param):
    value = input("    " + param + " (Y/N): ")
    if value == "Y":
        return True
    else:
        return False


def createOrganization(orgCalled):
    organization = Organization(called=orgCalled)
    print("Enter more details of the organization: long name, legal name, uri, emailSuffix, classifiers")
    print("Press Enter if not present.")
    organization.longName = getStrInput("Long name")
    organization.legalName = getStrInput("Legal name")
    organization.uri = getStrInput("Uri")
    organization.emailSuffix = getStrInput("Email Suffix")
    organization.classifiers = getStrArrInput("Classifiers")
    organization.addToDB()
    return organization

def findOrganization():
    orgCalled = input("Search for the organization you interacted with: ")
    organizationResults = Organization.findByCalled(orgCalled)
    if len(organizationResults) == 0:
        print(orgCalled + " is not in the database, please add it in")
        return createOrganization(orgCalled)
    else:
        print("Here are the organizations found: ")
        for i in range(0, len(organizationResults)):
            print("    {}. {}".format(str(i + 1), organizationResults[i].called))
        i = getIntInput("Type the index of the organization you interacted with: ")
        return organizationResults[i-1]


def createPerson(personCalled):
    person = Person(called=personCalled)
    print("Enter more details of the person: given name, maiden name, birth date, has user account, team member")
    print("Press Enter if not present.")
    person.givenName = getStrInput("Given name")
    person.surName = getStrInput("Surname")
    person.maidenName = getStrInput("Maiden name")
    person.gender = getStrInput("Gender")
    person.birthDate = getDateInput("Birth date")
    # person.hasUserAccount = getBoolInput("Do they have user account")
    # person.isTeamMember = getBoolInput("Are they a team member")
    person.addToDB()
    return person

def findPerson(i):
    personCalled = input("Search for person {} you interacted with: ".format(i+1))
    personResults = Person.findByCalled(personCalled)
    if len(personResults) == 0:
        print(personCalled + " is not in the database, please add it in")
        return createPerson(personCalled)
    else:
        print("Here are the persons found: ")
        for i in range(0, len(personResults)):
            print("    {}. {}".format(str(i + 1), personResults[i].called))
        i = getIntInput("Type the index of the person you interacted with: ")
        return personResults[i - 1]


def createContactCard(personUUID, organizationUUID):
    contactCard = ContactCard(person_uuid=personUUID, organization_uuid = organizationUUID)
    print("Enter more details of the contact card: title, email, mobile line, office direct line, start date, end date, role description, location")
    print("Press Enter if not present.")
    contactCard.title = getStrInput("Title")
    contactCard.email = getStrInput("Email")
    contactCard.mobileLine = getStrInput("Mobile line")
    contactCard.officeDirectLine = getStrInput("Office direct line")
    contactCard.startDate = getDateInput("Start date")
    contactCard.endDate = getDateInput("End date")
    contactCard.roleDescription = getStrInput("Role description")
    # TODO: contactCard.location_uuid
    contactCard.addToDB()

    return contactCard


def findContactCard(person, organization):
    contactCardResults = ContactCard.findByPersonAndOrganization(person.uuid, organization.uuid)
    if len(contactCardResults) == 0:
        print("The contact card of {} working at {} is not in the database, please add it in".format(person.called, organization.called))
        return createContactCard(person.uuid, organization.uuid)
    elif len(contactCardResults) == 1:
        return contactCardResults[0]
    else:
        print("Here are all the {} who works(ed) at {}: ".format(person.called, organization.called))
        for i in range(0, len(contactCardResults)):
            print("    {}. {}   {}  {}  {}".format(str(i + 1), person.givenName, person.surName, contactCardResults[i].title,  contactCardResults[i].email))
        i = getIntInput("Type the index of the contact card you want: ")
        return contactCardResults[i - 1]


def createInteractionMaterial(interaction, organization, i):
    material = InteractionMaterial(interaction_uuid=interaction.uuid, organization_uuid=organization.uuid)
    path = getStrInput("Path to file" + str(i + 1))
    # File name should not have"/" inside
    fileName = path.split("/")[-1]
    # file name should not have"." inside
    material.name = fileName.split(".")[0]
    material.fileType = fileName.split(".")[1]
    # The string components in the following line must not be None
    material.fileKey = organization.called + "/Interaction Material/" + interaction.date + "/" + material.name + "." + material.fileType
    material.url = S3Bucket.getUrl(material.fileKey)
    material.contactCard_uuids = interaction.contactCard_uuids
    S3Bucket.add(path, material.fileKey)
    material.addToDB()


def createVariableDocumentation(variableHandle):
    variable = VariableDocumentation(handle=variableHandle)
    print("Enter more details of the variable: complete name, acronym, description" )
    print("Press Enter if not present.")
    variable.completeName = getStrInput("Complete name")
    variable.acronym = getStrInput("Acronym")
    variable.description = getStrInput("Description")
    variable.addToDB()
    return variable


def findVariable(i):
    variableHandle = input("Search for handle of your variable {}: ".format(i + 1))
    variableResults = VariableDocumentation.findByHandle(variableHandle)
    if len(variableResults) == 0:
        print(variableHandle + " is not in the database, please add it in")
        return createVariableDocumentation(variableHandle)
    else:
        variableFound = variableResults[0]
        print("Variable handle: {}  Complete name: {}   Description: {}".format(variableFound.handle, variableFound.completeName, variableFound.description))
        chooseThisHandle = getBoolInput("Do you mean this variable")
        if chooseThisHandle:
            return variableFound
        else:
            print("Variable handles need to be unique. Search again.")
            return findVariable(i)



def createDataPoint(interaction, organization, i):
    dataPoint = CollectedDataPoint(interaction_uuid=interaction.uuid, organization_uuid=organization.uuid)
    variable = findVariable(i)
    print("Enter more details of the data point: time frame, value" )
    print("Press Enter if not present.")
    dataPoint.variableHandle = variable.handle
    dataPoint.timeFrame = getStrInput("Time frame")
    dataPoint.value = getStrInput("Value")
    dataPoint.variable_uuid = variable.uuid
    dataPoint.addToDB()


def addInteractionStepByStep():
    # link contact cards
    print("Follow the steps below to add an interaction.")
    interaction = Interaction()
    organization = findOrganization()
    contactCards = []
    numContact = getIntInput("How many people did you interact at this interaction: ")
    for i in range(numContact):
        person = findPerson(i)
        contactCards.append(findContactCard(person, organization))

    # interaction details
    print("Enter more details of the interaction: type, start time, end time, location")
    print("Press Enter not present.")
    interaction.interactionType = getStrInput("Interaction type")
    interaction.date = getDateInput("Date")
    interaction.contactCard_uuids = [contactCard.uuid for contactCard in contactCards]
    interaction.addToDB()
    print("INTERACTION CREATED.")

    # link materials
    numMaterial = getIntInput("How many materials do you want to add to this interaction: ")
    for i in range(numMaterial):
        createInteractionMaterial(interaction, organization, i)

    # link data points
    numDataPoint = getIntInput("How many data points do you want to add to this interaction: ")
    for i in range(numDataPoint):
        createDataPoint(interaction, organization, i)

    print("DONE!")
        

addInteractionStepByStep()
