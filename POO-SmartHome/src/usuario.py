class Usuario:
    def __init__(self, nombre, username, password, rol="estandar"):
        self.nombre = nombre
        self.username = username
        self.__password = password  # encapsulado
        self.rol = rol

    def mostrar_datos(self):
        return {
            "nombre": self.nombre,
            "username": self.username,
            "rol": self.rol
        }

    def cambiar_rol(self, nuevo_rol):
        self.rol = nuevo_rol
