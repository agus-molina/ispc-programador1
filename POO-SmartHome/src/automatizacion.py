import datetime

class Automatizacion:
    def __init__(self, id, nombre, estado, hora_activacion, hora_desactivacion):
        self.__id = id
        self.__nombre = nombre
        self.__estado = estado
        self.__hora_activacion = hora_activacion
        self.__hora_desactivacion = hora_desactivacion

    @property
    def id(self) -> int:
            return self.__id
        
    @property
    def nombre(self) -> str:
            return self.__nombre
        
    @property
    def estado(self) -> bool:
            return self.__estado
        
    @property
    def hora_activacion(self) -> datetime.time:
            return self.__hora_activacion
        
    @property
    def hora_desactivacion(self) -> datetime.time:
            return self.__hora_desactivacion

    def revisar_hora(self):
        hora_actual = datetime.now().time()
        if self._hora_activacion < self._hora_desactivacion:
            self.__estado = self.hora_activacion <= hora_actual < self._hora_desactivacion
        else:
            self.__estado = hora_actual >= self.hora_activacion or hora_actual < self._hora_desactivacion
