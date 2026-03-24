from abc import ABC, abstractmethod

class IAppBLL(ABC):
    @abstractmethod
    def create_db(self):
        pass
