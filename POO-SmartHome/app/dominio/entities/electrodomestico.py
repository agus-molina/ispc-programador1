from app.dominio.entities.dispositivo import Dispositivo

class Electrodomestico(Dispositivo):
    def __init__(self, id, nombre, estado=False, volumen=50, intensidad=None):
        super().__init__(id=id, nombre=nombre, tipo="electrodomestico", estado=estado)
        self.__volumen = volumen
        self.__intensidad = intensidad

    def subir_volumen(self, cantidad: int):
        if self.__volumen is not None:
            self.__volumen = min(100, self.__volumen + cantidad)

    def bajar_volumen(self, cantidad: int):
        if self.__volumen is not None:
            self.__volumen = max(0, self.__volumen - cantidad)

    def subir_intensidad(self, cantidad: int):
        if self.__intensidad is not None:
            self.__intensidad = min(100, self.__intensidad + cantidad)

    def bajar_intensidad(self, cantidad: int):
        if self.__intensidad is not None:
            self.__intensidad = max(0, self.__intensidad - cantidad)