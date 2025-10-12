from abc import ABC, abstractmethod
from typing import List, Optional
from app.dominio.entities.usuario import Usuario

class InterfaceUsuarioDAO(ABC):

    @abstractmethod
    def get(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, usuario: Usuario):
        pass

    @abstractmethod
    def update(self, usuario: Usuario):
        pass

    @abstractmethod
    def delete(self, id_usuario: int):
        pass