from abc import ABC, abstractmethod
from typing import List, Optional
from app.dominio.entities.luz import Luz

class InterfaceLuzDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, luz: Luz):
        pass

    @abstractmethod
    def update(self, luz: Luz):
        pass

    @abstractmethod
    def delete(self, id_dispositivo: int):
        pass