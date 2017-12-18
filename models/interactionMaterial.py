from database import connect
import uuid as uuidpkg
import psycopg2.extras
import psycopg2.extensions as exten

class InteractionMaterial:
    def __init__(self, name=None, fileType=None, uuid=None, organization_uuid=None, interaction_uuid=None, contactCard_uuids=[], url=None, fileKey=None):
        self.name = name
        self.fileType = fileType
        self.organization_uuid = organization_uuid
        self.uuid = uuidpkg.uuid4() if uuid is None else uuid
        self.interaction_uuid = interaction_uuid
        self.contactCard_uuids = contactCard_uuids
        self.url = url
        self.fileKey = fileKey # file name and file path on s3 bucket

        psycopg2.extras.register_uuid()

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO interactionMaterials (name, fileType, organization_uuid, uuid, interaction_uuid, '
                    'contactCard_uuids, url, fileKey) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.name, self.fileType, self.organization_uuid, self.uuid, self.interaction_uuid,
                     exten.adapt(self.contactCard_uuids), self.url, self.fileKey))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM interactionMaterials WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
