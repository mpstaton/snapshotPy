from database import connect


class ContactCard:
    def __init__(self, person_uuid=None, title=None, organization_uuid=None, email=None,
                 mobileLine=None, officeDirectLine=None, startDate=None, endDate=None,
                 roleDescription=None, location_uuid=None, uuid=None):
        self.person_uuid = person_uuid
        self.title = title
        self.organization_uuid = organization_uuid
        self.email = email
        self.mobileLine = mobileLine
        self.officeDirectLine = officeDirectLine
        self.startDate = startDate
        self.endDate = endDate
        self.roleDescription = roleDescription
        self.location_uuid = location_uuid
        self.uuid = uuid

    # the below code is an attempt to get scripting working with Postgres
    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO contactCards (person_uuid, title, organization_uuid, email, mobileLine, '
                    'officeDirectLine, startDate, endDate, roleDescription, location_uuid) VALUES (%s, %s, %s, %s, '
                    '%s, %s, %s, %s, %s, %s)',
                    (self.person_uuid, self.title, self.organization_uuid, self.email, self.mobileLine,
                     self.officeDirectLine, self.startDate, self.endDate, self.roleDescription, self.location_uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM "contactCards" WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
