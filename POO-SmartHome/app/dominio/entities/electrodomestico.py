from app.dominio.entities.dispositivo import Dispositivo

class Electrodomestico(Dispositivo):
    def __init__(self, id, nombre, estado, intensidad, volumen):
        super().__init__(id=id, nombre=nombre, tipo="electrodomestico", estado=estado, intensidad=intensidad, volumen=volumen)
        self._intensidad = intensidad
        self._volumen = volumen

    def subir_volumen(self, cantidad: int):
        if self._volumen is not None:
            self._volumen = min(100, self._volumen + cantidad)

    def bajar_volumen(self, cantidad: int):
        if self._volumen is not None:
            self._volumen = max(0, self._volumen - cantidad)

    def subir_intensidad(self, cantidad: int):
        if self._intensidad is not None:
            self._intensidad = min(100, self._intensidad + cantidad)

    def bajar_intensidad(self, cantidad: int):
        if self._intensidad is not None:
            self._intensidad = max(0, self._intensidad - cantidad)