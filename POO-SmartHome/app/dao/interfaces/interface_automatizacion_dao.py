from abc import ABC, abstractmethod
from abc import ABC, abstractmethod
from typing import List, Optional
from app.dominio.entities.automatizacion import Automatizacion

class InterfaceAutomatizacionDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, automatizacion: Automatizacion):
        pass

    @abstractmethod
    def update(self, automatizacion: Automatizacion):
        pass

    @abstractmethod
    def delete(self, id_automatizacion: int):
        pass