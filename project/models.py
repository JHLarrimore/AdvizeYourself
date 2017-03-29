# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return 'user email is {0}'.format(self.email)


class Email(db.Model):

    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    email_added_on = db.Column(db.DateTime, nullable=False)
    dob = db.Column(db.String, nullable=True)
    income = db.Column(db.Integer, nullable=True)
    age_at_retire = db.Column(db.Integer, nullable=True)
    yearlyContributions = db.Column(db.Integer, nullable=True)
    currentValue = db.Column(db.Integer, nullable=True)
    companyMatch = db.Column(db.Integer, nullable=True)

    def __init__(self, email):
        self.email = email
        self.email_added_on = datetime.datetime.now()
