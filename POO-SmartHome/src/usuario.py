from enum import Enum

class RolUsuario(Enum):
    ESTANDAR = "estandar"
    ADMIN = "admin"

class Usuario:
    def __init__(self, id: int, username: str, contrasena: str, correo: str, rol=RolUsuario.ESTANDAR):

        self.__username = username
        self.__contrasena = contrasena  
        self.__correo = correo
        self.__rol = rol

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def correo(self) -> str:
        return self.__correo
    
    @property
    def rol(self) -> RolUsuario:  # devuelve el enum, no un str
        return self.__rol
    
    def autenticar(self, input_contrasena: str) -> bool:
        """Verifica si la contrasena ingresada coincide con la registrada."""
        return self.__contrasena == input_contrasena
    
    def alternar_rol(self):
        if self.__rol == RolUsuario.ADMIN:
            self.__rol = RolUsuario.ESTANDAR
        else:
            self.__rol = RolUsuario.ADMIN

    def mostrar_datos(self) -> dict:
        return {
            "username": self.__username,
            "rol": self.__rol.value              #.value para obtener el valor del enum como cadena string legible
        }
