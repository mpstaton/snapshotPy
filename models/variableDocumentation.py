from database import connect
import uuid as uuidpkg
import psycopg2.extras


class VariableDocumentation:
    def __init__(self, handle=None, completeName=None, acronym=None, inputVariations=None,
                 description=None, uuid=None, data=None):
        self.handle = handle
        self.completeName = completeName
        self.acronym = acronym
        self.inputVariations = inputVariations
        self.description = description
        self.uuid = uuidpkg.uuid4() if uuid is None else uuid
        self.data = data

        psycopg2.extras.register_uuid()


    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO variableDocumentation (handle, completeName, acronym, inputVariations, '
                    'description, uuid, data) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (self.handle, self.completeName, self.acronym, self.inputVariations,
                     self.description, self.uuid, self.data))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM variableDocumentation WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    @classmethod
    def findByHandle(cls, handle):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM variableDocumentation WHERE handle=%s', (handle,))
                rows = cursor.fetchall()
                return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows]