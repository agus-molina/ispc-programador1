'''
MODULO QUE MANEJA AUTOMATIZACIONES
'''
from datetime import datetime
import datos

def modo_actual_programa():
    tiempo = datetime.now()
    # Modo NOCHE: entre las 00:00 y 06:00
    if 0 <= tiempo.hour < 6:
        return "NOCHE"
    # Modo MEDITACIÓN: entre las 15:00 y 16:00
    elif 15 <= tiempo.hour < 16:
        return "MEDITACIÓN"
    # Si no entra en ninguno de esos rangos, no hay modo definido
    else:
        return None

def ajuste_automatico(modo):
    mensajes = []
    if modo:
        for dispositivo in datos.inventario:
            tipo = dispositivo.get("tipo", "").lower()
            match modo:
                case "NOCHE":
                    if tipo in ("electrodomestico", "luz"):
                        dispositivo["estado"] = False
                        mensajes.append(f"El dispositivo {dispositivo['nombre']} se ha apagado.")
                    elif tipo == "camara":
                        dispositivo["estado"] = True
                        dispositivo["infrarrojo"] = True
                        mensajes.append(f"La cámara {dispositivo['nombre']} se ha activado con infrarrojo.")
                case "MEDITACION":
                    if tipo == "luz":
                        dispositivo["intensidad"] = 10
                        mensajes.append(f"La intensidad del dispositivo {dispositivo['nombre']} se ha ajustado.")
    return mensajes
