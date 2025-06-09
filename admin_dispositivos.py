'''
MODULO QUE MANEJA DISPOSITIVOS
'''

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
    
# Validación Función eliminar dispositivo
def eliminar_dispositivo(inventario, indice):
    if 0 <= indice < len(inventario):
        eliminado = inventario.pop(indice)
        print(f"Dispositivo '{eliminado.get('nombre')}' eliminado con éxito.")
    else:
        print("Índice fuera de rango. No se pudo eliminar.")


