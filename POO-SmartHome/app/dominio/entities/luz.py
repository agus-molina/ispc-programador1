from app.dominio.entities.dispositivo import Dispositivo

class Luz(Dispositivo):
    def __init__(self, id, nombre, estado=False, intensidad=0):
        super().__init__(id=id, nombre=nombre, tipo="luz", estado=estado)
        self.__intensidad = intensidad

    def subir_intensidad(self, cantidad: int):
        if self.__intensidad is not None:
            self.__intensidad = min(100, self.__intensidad + cantidad)

    def bajar_intensidad(self, cantidad: int):
        if self.__intensidad is not None:
            self.__intensidad = max(0, self.__intensidad - cantidad)
