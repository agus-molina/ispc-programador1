from abc import ABC, abstractmethod
from app.dominio.entities.dispositivo import Dispositivo

class InterfaceDispositivoDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, dispositivo: Dispositivo, id_usuario: int):
        pass

    @abstractmethod
    def update(self, dispositivo: Dispositivo):
        pass

    @abstractmethod
    def delete(self, id_dispositivo: int):
        pass