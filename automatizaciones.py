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
    tipo = None
    for dispositivo in inventario:
        tipo = dispositivo["tipo"]
        if modo == "NOCHE":
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = False 
            elif tipo == "camara":
                dispositivo["estado"] = True
        else:
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = True
            elif tipo == "camara":
                dispositivo["estado"] = False
