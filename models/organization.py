from db import db

class OrganizationModel(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.Integer, primary_key=True)
    called = db.Column(db.String(80))
    longName = db.Column(db.String(80))
    legalName = db.Column(db.String(80))
    uri = db.Column(db.String(80))
    emailSuffix = db.Column(db.String(80))

    def __init__(self, called, longName, legalName, uri, emailSuffix):
        self.called = called
        self.longName = longName
        self.legalName = legalName
        self.uri = uri
        self.emailSuffix = emailSuffix

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_called(cls, called):
        return cls.query.filter_by(called=called).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()