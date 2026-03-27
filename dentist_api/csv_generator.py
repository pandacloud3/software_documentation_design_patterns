import csv
import random
from datetime import datetime, timedelta

def generate_csv(filename='clinic_data.csv', rows=1005):
    dentists = [
        {"name": "Ivan Ivanov", "license": "LIC-1001", "spec": "Surgeon", "cabinet": 101},
        {"name": "Anna Petrenko", "license": "LIC-1002", "spec": "Therapist", "cabinet": 102},
        {"name": "Oleg Shevchenko", "license": "LIC-1003", "spec": "Orthodontist", "cabinet": 103}
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['DentistName', 'LicenseNumber', 'Specialization', 'Cabinet', 
                         'PatientName', 'InsuranceNumber', 'PatientPhone', 'AppointmentDate', 'Status'])

        for i in range(rows):
            dentist = random.choice(dentists)
            patient_name = f"Patient_{i}"
            insurance = f"INS-{random.randint(10000, 99999)}"
            phone = f"+38050{random.randint(1000000, 9999999)}"
            
            days_offset = random.randint(1, 60)
            app_date = (datetime.now() + timedelta(days=days_offset)).strftime('%Y-%m-%d %H:%M')
            status = random.choice(['Scheduled', 'Completed', 'Cancelled'])

            writer.writerow([
                dentist["name"], dentist["license"], dentist["spec"], dentist["cabinet"],
                patient_name, insurance, phone, app_date, status
            ])

    print(f"Файл {filename} успішно згенеровано на {rows} рядків!")

if __name__ == '__main__':
    generate_csv()