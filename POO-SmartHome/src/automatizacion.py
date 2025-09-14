class Automatizacion:
    def __init__(self, modo="DIA"):
        self.modo = modo

    def ajustar_dispositivos(self, dispositivos):
        mensajes = []
        for d in dispositivos:
            if self.modo == "NOCHE":
                if d.tipo in ["electrodomestico", "luces"]:
                    d.apagar()
                    mensajes.append(f"{d.nombre} apagado")
                elif d.tipo == "camara":
                    d.encender()
                    mensajes.append(f"{d.nombre} encendida")
            else:
                if d.tipo in ["electrodomestico", "luces"]:
                    d.encender()
                    mensajes.append(f"{d.nombre} encendido")
                elif d.tipo == "camara":
                    d.apagar()
                    mensajes.append(f"{d.nombre} apagada")
        return mensajes
