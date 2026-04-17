from datetime import datetime
from core.interfaces import IBusinessLogic, IDataRepository
from core.models import Appointment

class ClinicService(IBusinessLogic):
    def __init__(self, repository: IDataRepository):
        self.repository = repository 

    def process_and_import_data(self, file_path):
        raw_data = self.repository.read_csv_data(file_path)
        
        for row in raw_data:
            dentist = self.repository.get_or_create_dentist(
                name=row['DentistName'],
                license_num=row['LicenseNumber'],
                spec=row['Specialization'],
                cabinet=int(row['Cabinet'])
            )
            
            patient = self.repository.get_or_create_patient(
                name=row['PatientName'],
                insurance=row['InsuranceNumber'],
                phone=row['PatientPhone']
            )
            
            app_date = datetime.strptime(row['AppointmentDate'], '%Y-%m-%d %H:%M')
            appointment = Appointment(
                date_time=app_date,
                status=row['Status'],
                dentist_id=dentist.id,
                patient_id=patient.id
            )
            
            self.repository.save_appointment(appointment)
            
        self.repository.commit()
        return len(raw_data)