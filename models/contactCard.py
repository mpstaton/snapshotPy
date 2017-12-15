from database import connect
import uuid
import psycopg2.extras
import psycopg2.extensions as exten

class ContactCard:
    def __init__(self, person_uuid=None, title=None, organization_uuid=None, email=None,
                 mobileLine=None, officeDirectLine=None, startDate=None, endDate=None,
                 roleDescription=None, location_uuid=None, uuid=uuid.uuid4()):
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

        psycopg2.extras.register_uuid()


       # json data model for ContactCards
       # {personalEmails: [""],
       # currentMobileNumber: "",
       #
       # "currentRole":
       #      {
       #          "title" : "",
       #          "organization_uuid" : "",
       #          "email" : "",
       #          "mobileLine" : "",
       #          "startDate" : "",
       #          "roleDescription" : "",
       #          "location": {
       #              "location_uuid": "",
       #              "locationName": "",
       #              "locationAddress": ""
       #          }
       #      },
       #  "previousRoles": [
       #      {
       #          "title" : "",
       #          "organization_uuid" : "",
       #          "email" : "",
       #          "startDate" : "",
       #          "endDate"
       #          "roleDescription" : "",
       #          "location": {
       #              "location_uuid": "",
       #              "locationName": "",
       #              "locationAddress": ""
       #          }
       #      }
       #  ]
       #
       #
       # }


    def addToDB(self):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO contactCards (person_uuid, title, organization_uuid, email, mobileLine, '
                    'officeDirectLine, startDate, endDate, roleDescription, location_uuid, uuid) VALUES (%s, %s, %s, '
                    '%s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.person_uuid, self.title, self.organization_uuid, self.email, self.mobileLine,
                     self.officeDirectLine, self.startDate, self.endDate, self.roleDescription, self.location_uuid, self.uuid))

    @classmethod
    def getByUUID(cls, uuid):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM contactCards WHERE uuid=%s', (uuid, ))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],row[11])

    @classmethod
    def getByEmail(cls, email):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM contactCards WHERE email=%s', (email,))
                row = cursor.fetchone()
                return cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],row[11])

    @classmethod
    def findByPersonAndOrganization(cls, personUUID, organizationUUID):
        with connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM contactCards WHERE person_uuid=%s And organization_uuid=%s', (personUUID, organizationUUID, ))
                rows = cursor.fetchall()
                return [cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]) for row in rows]