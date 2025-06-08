'''
MODULO QUE MANEJA AUTOMATIZACIONES
'''
from datetime import datetime

def modo_actual_programa():
    tiempo = datetime.now()
    if  7 <= tiempo.hour < 19:
        return "DIA"
    else:
        return "NOCHE"
    
def ajuste_automatico(inventario, modo):
    if modo == "NOCHE":
        for dispositivo in inventario:
            if dispositivo.get("tipo").lower() == "electrodomestico" or dispositivo.get("tipo").lower() == "luces":
                dispositivo["estado"] = False
            elif dispositivo.get("tipo") == "camara":
                dispositivo["estado"] = True