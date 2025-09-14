class Dispositivo:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = False
        self.intensidad = 1
        self.volumen = 0
        self.infrarrojo = False

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False
