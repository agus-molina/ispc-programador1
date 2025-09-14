'''
MODULO QUE MANEJA DISPOSITIVOS
'''

import EV3.datos as datos

def listar_dispositivos():
    if not datos.inventario:
        print("No hay dispositivos vinculados aún.")
        return
    print("Listado Completo de Dispositivos:")
    for dispositivo in datos.inventario:
            print(f'''\nID: {dispositivo.get('id')}
            Nombre: {dispositivo.get('nombre')}
            Tipo: {dispositivo.get('tipo')}
            Estado: {dispositivo.get('estado')}''')

def buscar_dispositivo(nombre):
    nombre_busqueda = nombre.strip().lower()
    for dispositivo in datos.inventario:
        if dispositivo.get("nombre", "").lower() == nombre_busqueda:
            print(f"Dispositivo encontrado:")
            print(f"ID: {dispositivo['id']}, Nombre:{dispositivo['nombre']}, Tipo: {dispositivo['tipo']}, Estado: {dispositivo['estado']}")
            return dispositivo
    print(f"No se encontró un dispositivo con ese nombre.")
    return None

def agregar_dispositivo():
    nombre = input('Ingresa el Nombre del Dispositivo a vincular: ').strip().lower()
    tipo = input('Ingresa el tipo de dispositivo (ELECTRODOMESTICO / LUCES / CAMARA): ').strip().lower()
    dispositivo = {
                    "id": datos.contador_id,
                   "nombre": nombre,
                   "tipo": tipo,
                   "estado": False,
                   "intensidad": 1,
                   "volumen": 0,
                   "infrarrojo": False
                   }
    datos.inventario.append(dispositivo)
    datos.contador_id += 1
    print(f'''Dispositivo vinculado con Éxito:
         ID: {dispositivo.get('id')}
         Nombre: {dispositivo.get('nombre')}
         Tipo: {dispositivo.get('tipo')}
         Estado: {dispositivo.get('estado')}
         Intensidad: {dispositivo.get('intensidad')}
         Volumen: {dispositivo.get('volumen')}
         Infrarrojo: {dispositivo.get('infrarrojo')}''')
    
# Validación Función eliminar dispositivo
def eliminar_dispositivo(id_dispositivo):
    for i, d in enumerate(datos.inventario):
        if d.get('id') == id_dispositivo:
            eliminado = datos.inventario.pop(i)
            print(f"Dispositivo '{eliminado.get('nombre')}' eliminado con éxito.")
            return True
    print("No se encontró un dispositivo con ese ID. No se pudo eliminar.")
    return False


