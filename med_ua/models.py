""" creating models for database """
from sqlalchemy.sql import func
from med_ua.extentions import db

# Create a models
class Record(db.Model):
    """ adding record model """
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

class Doctor(db.Model):
    """ creating doctor model """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    years_xp = db.Column(db.Integer)
    name = db.Column(db.String(100))
    specialization = db.Column(db.String(100))
    records = db.relationship('Record', backref='recs')