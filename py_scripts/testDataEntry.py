from models.collectedDataPoint import CollectedDataPoint
from models.contactCard import ContactCard
from models.interaction import Interaction
from models.interactionMaterial import InteractionMaterial
from models.organization import Organization
from models.person import Person
from models.variableDocumentation import VariableDocumentation
import uuid



newDataPoint = CollectedDataPoint(variableHandle="testHandle", value=3)
newDataPoint.addToDB()

printNew = CollectedDataPoint.getByUUID(newDataPoint.uuid)
print(str(printNew.uuid) + printNew.variableHandle)



newContactCard = ContactCard(
    person_uuid=uuid.UUID('2258da15-12e1-45b3-bae6-9214cc632636'),
    email='don@learnstart',
    mobileLine='917-514-7903',
    startDate='201703',
    organization_uuid=uuid.UUID('ed06d172-5ea7-4be1-b571-69ccc956b44f')
)
newContactCard.addToDB()
printNew = ContactCard.getByUUID(newContactCard.uuid)
print(str(printNew.uuid))
printNew = ContactCard.getByEmail(newContactCard.email)
print(str(printNew.uuid))





newInteraction = Interaction(interactionMaterial_uuids=[uuid.UUID('2cc7b063-aa77-404d-a270-fe036548a932'),
                                                        uuid.UUID('d59d4a55-36fc-4757-94d5-4355404d47bb')])
newInteraction.addToDB()

printNew = Interaction.getByUUID(newInteraction.uuid)
print(str(printNew.uuid) + str(printNew.interactionMaterial_uuids[0]))





newInteractionMaterial = InteractionMaterial(name="testinteractionmaterial")
newInteractionMaterial.addToDB()

printNew = InteractionMaterial.getByUUID(newInteractionMaterial.uuid)
print(str(printNew.uuid) + printNew.name)




newOrg = Organization(called="testOrg", longName="test organization")
newOrg.addToDB()

printNew = Organization.getByUUID(newOrg.uuid)
print(str(printNew.uuid) + printNew.called)




newPerson = Person(called="Don", givenName="Donald", surName="Burton", gender="Male", hasUserAccount=True, isTeamMember=True)
newPerson.addToDB()

printNew = Person.getByUUID(newPerson.uuid)
print(str(printNew.uuid) + printNew.gender)


newVarDoc = VariableDocumentation(handle='test', inputVariations=['inputvar1', 'inputvar2'])
newVarDoc.addToDB()

printNew = VariableDocumentation.getByUUID(newVarDoc.uuid)
print(str(printNew.uuid) + printNew.inputVariations[0])