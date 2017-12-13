
from models.contactCard import ContactCard

newContactCard = ContactCard(
    person_uuid='2258da15-12e1-45b3-bae6-9214cc632636',
    email='don@learnstart',
    mobileLine='917-514-7903',
    startDate='201703',
    organization_uuid='ed06d172-5ea7-4be1-b571-69ccc956b44f'
)

newContactCard.addToDB()

