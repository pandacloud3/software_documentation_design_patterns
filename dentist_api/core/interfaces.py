from abc import ABC, abstractmethod

class IDataRepository(ABC):
    @abstractmethod
    def read_csv_data(self, file_path):
        pass

    @abstractmethod
    def get_or_create_dentist(self, name, license_num, spec, cabinet):
        pass

    @abstractmethod
    def get_or_create_patient(self, name, insurance, phone):
        pass

    @abstractmethod
    def save_appointment(self, appointment):
        pass

    @abstractmethod
    def commit(self):
        pass

class IBusinessLogic(ABC):
    @abstractmethod
    def process_and_import_data(self, file_path):
        pass