'''
MODULO QUE MANEJA AUTOMATIZACIONES
'''
from datetime import datetime
import EV3.datos as datos

def modo_actual_programa():
    tiempo = datetime.now()
    if  7 <= tiempo.hour < 19:
        return "DIA"
    else:
        return "NOCHE"

def ajuste_automatico(modo):
    mensajes = []
    for dispositivo in datos.inventario:
        tipo = dispositivo.get("tipo", "").lower()
        if modo == "NOCHE":
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = False
                mensajes.append(f"El dispositivo {dispositivo['nombre']} se ha apagado.")
            elif tipo == "camara":
                dispositivo["estado"] = True
                mensajes.append(f"La cámara {dispositivo['nombre']} se ha activado.")
        else:  # DÍA
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = True
                mensajes.append(f"El dispositivo {dispositivo['nombre']} se ha encendido.")
            elif tipo == "camara":
                dispositivo["estado"] = False
                mensajes.append(f"La cámara {dispositivo['nombre']} se ha apagado.")
    return mensajes
