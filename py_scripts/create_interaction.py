
from models.interaction import Interaction
import uuid

newInteraction = Interaction(interactionMaterial_uuids=[uuid.UUID('2cc7b063-aa77-404d-a270-fe036548a932'), uuid.UUID('d59d4a55-36fc-4757-94d5-4355404d47bb')],
                             contactCard_uuids=[uuid.UUID('2cc7b063-aa77-404d-a270-fe036548a932'), uuid.UUID('d59d4a55-36fc-4757-94d5-4355404d47bb')])

newInteraction.addToDB()
