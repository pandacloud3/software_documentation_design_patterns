from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dentist(db.Model):
    __tablename__ = 'dentists'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), unique=True, nullable=False)
    specialization = db.Column(db.String(100))
    cabinet_number = db.Column(db.Integer)
    
    appointments = db.relationship('Appointment', backref='dentist', lazy=True)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    insurance_number = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20))
    
    dentist_id = db.Column(db.Integer, db.ForeignKey('dentists.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)