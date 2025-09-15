class Usuario:
    def __init__(self, id, username, contraseña, correo, rol="estandar"):
        self.__id = id
        self.__username = username
        self.__contraseña = contraseña
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
    def rol(self) -> str:
        return self.__rol
    
    def autenticar(self, input_contraseña: str) -> bool:
        """Verifica si la contraseña ingresada coincide con la registrada."""
        return self.__contraseña == input_contraseña
    
    def alternar_rol(self):
        if self.__rol == "admin":
            self.__rol = "estandar"
        else:
            self.__rol = "admin"

    def mostrar_datos(self) -> dict:
        return {
            "username": self.__username,
            "rol": self.__rol
        }
