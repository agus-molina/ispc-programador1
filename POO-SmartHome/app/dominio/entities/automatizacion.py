import datetime

class Automatizacion:
    def __init__(self, id, nombre, estado, hora_activacion, hora_desactivacion):
        self._id = id
        self._nombre = nombre
        self._estado = estado
        self._hora_activacion = hora_activacion
        self._hora_desactivacion = hora_desactivacion

    @property
    def id(self) -> int:
            return self._id
        
    @property
    def nombre(self) -> str:
            return self._nombre
        
    @property
    def estado(self) -> bool:
            return self._estado
        
    @property
    def hora_activacion(self) -> datetime.time:
            return self._hora_activacion
        
    @property
    def hora_desactivacion(self) -> datetime.time:
            return self._hora_desactivacion

    @id.setter
    def id(self, value: int):
        if self._id is None:
            self._id = value
        else:
            raise AttributeError("El ID no puede modificarse una vez asignado.")
    
    def activar(self):
          self._estado = True

    def desactivar(self):
          self._estado = False

    def revisar_hora(self):
        hora_actual = datetime.now().time()
        if self._hora_activacion < self._hora_desactivacion:
            self._estado = self._hora_activacion <= hora_actual < self._hora_desactivacion
        else:
            self._estado = hora_actual >= self._hora_activacion or hora_actual < self._hora_desactivacion
