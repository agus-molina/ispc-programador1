from app.dominio.entities.dispositivo import Dispositivo
        
class Camara(Dispositivo):
    def __init__(self, id, nombre, estado, infrarrojo):
        super().__init__(id=id, nombre=nombre, tipo="camara", estado=estado, infrarrojo=infrarrojo)
        self._infrarrojo = infrarrojo

    def interruptor_infrarrojo(self):
        if self._infrarrojo is not None:
            self._infrarrojo = not self._infrarrojo