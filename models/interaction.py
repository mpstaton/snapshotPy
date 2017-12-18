from database import connect
import uuid as uuidpkg
import psycopg2.extras
import psycopg2.extensions as exten

class Interaction:
    # interactionMaterial_uuids and contactCard_uuids can't be None, as the adaptor of uuid[] doesn't adapt None type
    def __init__(self, location_uuid=None, interactionType=None, startTime=None, endTime=None,
                 uuid=uuidpkg.uuid4(), interactionMaterial_uuids=[], contactCard_uuids=[], date=None):
        self.location_uuid = location_uuid
        self.interactionType = interactionType
        self.startTime = startTime
        self.endTime = endTime
        self.uuid = uuid
        self.interactionMaterial_uuids = interactionMaterial_uuids
        self.contactCard_uuids = contactCard_uuids
        self.date = date

        psycopg2.extras.register_uuid()

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO interactions (location_uuid, interactionType, startTime, endTime, uuid, '
                    'interactionMaterial_uuids, contactCard_uuids, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.location_uuid, self.interactionType, self.startTime, self.endTime, self.uuid,
                     exten.adapt(self.interactionMaterial_uuids), exten.adapt(self.contactCard_uuids), self.date))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM interactions WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])