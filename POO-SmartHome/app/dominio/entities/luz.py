from app.dominio.entities.dispositivo import Dispositivo

class Luz(Dispositivo):
    def __init__(self, id, nombre, estado, intensidad):
        super().__init__(id=id, nombre=nombre, tipo="luz", estado=estado, intensidad=intensidad)
        self._intensidad = intensidad

    def subir_intensidad(self, cantidad: int):
        if self._intensidad is not None:
            self._intensidad = min(100, self._intensidad + cantidad)

    def bajar_intensidad(self, cantidad: int):
        if self._intensidad is not None:
            self._intensidad = max(0, self._intensidad - cantidad)
