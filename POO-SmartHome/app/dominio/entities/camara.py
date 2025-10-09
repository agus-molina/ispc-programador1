from app.dominio.entities.dispositivo import Dispositivo
        
class Camara(Dispositivo):
    def __init__(self, id, nombre, estado=False, infrarrojo=False):
        super().__init__(id=id, nombre=nombre, tipo="camara", estado=estado)
        self.__infrarrojo = infrarrojo

    def interruptor_infrarrojo(self):
        if self.__infrarrojo is not None:
            self.__infrarrojo = not self.__infrarrojo