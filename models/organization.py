from database import connect
import uuid as uuidpkg
import psycopg2.extras


class Organization:
    def __init__(self, called=None, longName=None, legalName=None, uri=None, emailSuffix=None, uuid=None,
                 classifiers=None):
        self.called = called
        self.longName = longName
        self.legalName = legalName
        self.uri = uri
        self.emailSuffix = emailSuffix
        self.uuid = uuidpkg.uuid4() if uuid is None else uuid
        self.classifiers = classifiers

        psycopg2.extras.register_uuid()

    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO organizations (called, longName, legalName, uri, emailSuffix, uuid, classifiers) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (self.called, self.longName, self.legalName, self.uri, self.emailSuffix, self.uuid, self.classifiers))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM organizations WHERE uuid=%s', (uuid,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    @classmethod
    # Case insensitive search by called
    def findByCalled(cls, called):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM organizations WHERE called ILIKE %s', ("%" + called + "%", ))
                rows = cursor.fetchall()
                return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in rows]




# class Company(Organization):
#     def __init__(self, called, longName, legalName, uri, emailSuffix, dataRegistered):
#         super().__init__(called, longName, legalName, uri, emailSuffix, dataRegistered)
#
#
# class PortfolioCompany(Company):
#     def __init__(self, called="", longName="", legalName="", uri="", emailSuffix="", dataRegistered=""):
#         super().__init__(called, longName, legalName, uri, emailSuffix, dataRegistered)
#
#
# makeSchool = PortfolioCompany(called="MakeSchool", legalName="Make Games With Us", uri="http://makeschool.com")
#
# print(makeSchool.legalName)