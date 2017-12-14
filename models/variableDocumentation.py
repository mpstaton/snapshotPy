from database import connect
import uuid
import psycopg2.extras


class VariableDocumentation:
    def __init__(self, handle=None, completeName=None, acronym=None, inputVariations=None, classifiers=None,
                 description=None, uuid=uuid.uuid4()):
        self.handle = handle
        self.completeName = completeName
        self.acronym = acronym
        self.inputVariations = inputVariations
        self.classifiers = classifiers
        self.description = description
        self.uuid = uuid

        psycopg2.extras.register_uuid()


    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO variableDocumentation (handle, completeName, acronym, inputVariations, classifiers, '
                    'description, uuid) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (self.handle, self.completeName, self.acronym, self.inputVariations, self.classifiers,
                     self.description, self.uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM variableDocumentation WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])