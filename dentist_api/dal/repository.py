import csv
from core.interfaces import IDataRepository
from core.models import db, Dentist, Patient, Appointment

class SqlRepository(IDataRepository):
    def read_csv_data(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def get_or_create_dentist(self, name, license_num, spec, cabinet):
        dentist = Dentist.query.filter_by(license_number=license_num).first()
        if not dentist:
            dentist = Dentist(full_name=name, license_number=license_num, specialization=spec, cabinet_number=cabinet)
            db.session.add(dentist)
            db.session.flush()
        return dentist

    def get_or_create_patient(self, name, insurance, phone):
        patient = Patient.query.filter_by(insurance_number=insurance).first()
        if not patient:
            patient = Patient(full_name=name, insurance_number=insurance, phone=phone)
            db.session.add(patient)
            db.session.flush()
        return patient

    def save_appointment(self, appointment):
        db.session.add(appointment)

    def commit(self):
        db.session.commit()

    def get_all_dentists(self):
        return Dentist.query.all()

    def get_dentist_by_id(self, dentist_id):
        return Dentist.query.get(dentist_id)

    def delete_dentist(self, dentist_id):
        dentist = self.get_dentist_by_id(dentist_id)
        if dentist:
            Appointment.query.filter_by(dentist_id=dentist_id).delete()
            db.session.delete(dentist)
            db.session.commit()