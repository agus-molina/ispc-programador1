class Dispositivo:
    def __init__(self,
                 id,
                 nombre,
                 tipo,
                 estado=False,
                 intensidad: int | None = None,
                 volumen: int | None = None,
                 infrarrojo: bool | None = None):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo
        self._estado = estado
        self._intensidad = intensidad
        self._volumen = volumen
        self._infrarrojo = infrarrojo

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @property
    def estado(self) -> bool:
        return self._estado

    @property
    def intensidad(self) -> bool:
        return self._intensidad

    @property
    def volumen(self) -> bool:
        return self._volumen

    @property
    def infrarrojo(self) -> bool:
        return self._infrarrojo

    @id.setter
    def id(self, value: int):
        if self._id is None:
            self._id = value
        else:
            raise AttributeError("El ID no puede modificarse una vez asignado.")

    def encender(self):
        self._estado = True

    def apagar(self):
        self._estado = False