from database import connect


class Interaction:
    def __init__(self, location_uuid=None, interactionType=None, startTime=None, endTime=None,
                 uuid=None, interactionMaterial_uuids=None, contactCard_uuids=None):
        self.location_uuid = location_uuid
        self.interactionType = interactionType
        self.startTime = startTime
        self.endTime = endTime
        self.uuid = uuid
        self.interactionMaterial_uuids = interactionMaterial_uuids
        self.contactCard_uuids = contactCard_uuids

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO interactions (location_uuid, interactionType, startTime, endTime, '
                    'interactionMaterial_uuids, contactCard_uuids) VALUES (%s, %s, %s, %s, ["2cc7b063-aa77-404d-a270-fe036548a932", "d59d4a55-36fc-4757-94d5-4355404d47bb"]::uuid[], %s)',
                    (self.location_uuid, self.interactionType, self.startTime, self.endTime, self.contactCard_uuids))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM interactions WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6])
