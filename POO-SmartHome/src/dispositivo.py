class Dispositivo:
    def __init__(self,
                    id,
                    nombre,
                    tipo,
                    estado = False,
                    intensidad: int | None = None,
                    volumen: int | None = None,
                    infrarrojo: bool | None = None
                ):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado
        self.__intensidad = intensidad
        self.__volumen = volumen
        self.__infrarrojo = infrarrojo

    @property
    def id(self) -> int:
            return self.__id
        
    @property
    def nombre(self) -> str:
            return self.__nombre
    
    @property
    def tipo(self) -> str:
            return self.__tipo
        
    @property
    def estado(self) -> bool:
            return self.__estado

    def encender(self):
        self.__estado = True

    def apagar(self):
        self.__estado = False

class Camara(Dispositivo):
    def __init__(self, id, nombre, estado=False, infrarrojo=False):
        super().__init__(id=id, nombre=nombre, tipo="camara", estado=estado)
        self.__infrarrojo = infrarrojo

    def interruptor_infrarrojo(self):
        if self.__infrarrojo is not None:
            self.__infrarrojo = not self.__infrarrojo

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
