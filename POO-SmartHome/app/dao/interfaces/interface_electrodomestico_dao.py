from abc import ABC, abstractmethod
from typing import List, Optional
from app.dominio.entities.Electrodomestico import Electrodomestico

class InterfaceElectrodomesticoDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, electrodomestico: Electrodomestico):
        pass

    @abstractmethod
    def update(self, electrodomestico: Electrodomestico):
        pass

    @abstractmethod
    def delete(self, id_dispositivo: int):
        pass