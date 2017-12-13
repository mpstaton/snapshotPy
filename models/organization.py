from database import connect


class Organization:
    def __init__(self, called=None, longName=None, legalName=None, uri=None, emailSuffix=None, uuid=None,
                 classifiers=None):
        self.called = called
        self.longName = longName
        self.legalName = legalName
        self.uri = uri
        self.emailSuffix = emailSuffix
        self.uuid = uuid
        self.classifiers = classifiers

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO organizations (called, longName, legalName, uri, emailSuffix, classifiers) VALUES ('
                    '%s, %s, %s, %s, %s, %s)',
                    (self.called, self.longName, self.legalName, self.uri, self.emailSuffix, self.classifiers))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM organizations WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
