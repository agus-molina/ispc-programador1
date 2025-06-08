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
def ajuste_automatico(inventario, modo):
    for dispositivo in inventario:
        tipo = dispositivo.get("tipo", "").lower()
        if modo == "NOCHE":
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = False 
            elif tipo == "camara":
                dispositivo["estado"] = True
        elif modo == "DIA":
            if tipo in ["electrodomestico", "luces"]:
                dispositivo["estado"] = True
            elif tipo == "camara":
                dispositivo["estado"] = False
