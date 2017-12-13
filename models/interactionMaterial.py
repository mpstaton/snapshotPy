from database import connect

class InteractionMaterial:
    def __init__(self, name=None, fileType=None, uuid=None, organization_uuid=None, interaction_uuid=None, contactCard_uuid=None):
        self.name = name
        self.fileType = fileType
        self.organization_uuid = organization_uuid
        self.uuid = uuid
        self.interaction_uuid = interaction_uuid
        self.contactCard_uuid = contactCard_uuid

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO interactionMaterials (name, fileType, organization_uuid, interaction_uuid, '
                    'contactCard_uuid) VALUES (%s, %s, %s, %s, %s)',
                    (self.name, self.fileType, self.organization_uuid, self.interaction_uuid,
                     self.contactCard_uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM interactionMaterials WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6])
