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
    def __init__(self, tipo = "camara"):
        super()

class Luz(Dispositivo):
    def __init__(self, tipo = "luz"):
        super()

    def subir_intensidad(self, cantidad):
        pass
    def bajar_intensidad(self, cantidad):
        pass  
    
class Electrodomestico(Dispositivo):
    def __init__(self, tipo = "electrodomestico"):
        super()