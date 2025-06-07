from datetime import datetime

def modo_actual_programa():
    tiempo = datetime.now()
    if  7 <= tiempo.hour < 19:
        return "DIA"
    else:
        return "NOCHE"
    
def mostrar_menu():
    print('''\n         _Menú Principal_ 
        1) Listar Dispositivos Vinculados
        2) Buscar Dispositivos
        3) Agregar Nuevo Dispositivo
        4) Eliminar Dispositivo
        5) Salir del Sistema''')
    
def listar_dispositivos(inventario):
    if not inventario:
        print("No hay dispositivos vinculados aún.")
    else:
        print("Listado Completo de Dispositivos:")
        for i, dispositivo in enumerate(inventario):
            print(f'''\n{i + 1} - ID: {dispositivo.get('id')}
            Nombre: {dispositivo.get('nombre')}
            Tipo: {dispositivo.get('tipo')}
            Estado: {dispositivo.get('estado')}''')

def buscar_dispositivo(inventario, nombre):
    for dispositivo in inventario:
        if dispositivo.get("nombre") == nombre:
            return dispositivo
    return None
        
def agregar_dispositivo(inventario, contador_id):
    nombre = input('Ingresa el Nombre del Dispositivo a vincular: ').strip().lower()
    tipo = input('Ingresa el tipo de dispositivo (ELECTRODOMESTICO / LUCES / CAMARA): ').strip().lower()
    dispositivo = {
                    "id": contador_id,
                   "nombre": nombre,
                   "tipo": tipo,
                   "estado": False,
                   "intensidad": 1,
                   "volumen": 0,
                   "infrarrojo": False
                   }
    inventario.append(dispositivo)
    print(f'''Dispositivo vinculado con Éxito:
         ID: {dispositivo.get('id')}
         Nombre: {dispositivo.get('nombre')}
         Tipo: {dispositivo.get('tipo')}
         Estado: {dispositivo.get('estado')}
         Intensidad: {dispositivo.get('intensidad')}
         Volumen: {dispositivo.get('volumen')}
         Infrarrojo: {dispositivo.get('infrarrojo')}''')
    
def eliminar_dispositivo(inventario, id_a_eliminar):
    for i, dispositivo in enumerate(inventario):
        if dispositivo.get('id') == id_a_eliminar:
            del inventario[i]
            return True
    return False

def ajuste_automatico(inventario, modo):
    if modo == "NOCHE":
        for dispositivo in inventario:
            if dispositivo.get("tipo").lower() == "electrodomestico" or dispositivo.get("tipo").lower() == "luces":
                dispositivo["estado"] = False
            elif dispositivo.get("tipo") == "camara":
                dispositivo["estado"] = True