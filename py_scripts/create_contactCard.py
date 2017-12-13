
from models.contactCard import ContactCard
from models.person import Person

person = Person.getByUUID('2258da15-12e1-45b3-bae6-9214cc632636')
newContactCard = ContactCard(
    person_uuid=person.uuid,
    email='don@learnstart',
    mobileLine='917-514-7903',
    startDate='201703',
    organization_uuid='ed06d172-5ea7-4be1-b571-69ccc956b44f'
)

newContactCard.addToDB()

