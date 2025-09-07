'''
MODULO QUE MANEJA DISPOSITIVOS
'''
import datos


def listar_dispositivos():
    if not datos.inventario:
        print("No hay dispositivos vinculados aún.")
    else:
        print("Listado Completo de Dispositivos:")
        for i, dispositivo in enumerate(datos.inventario):
            print(f'''\n{i + 1} - ID: {dispositivo.get('id')}
            Nombre: {dispositivo.get('nombre')}
            Tipo: {dispositivo.get('tipo')}
            Estado: {dispositivo.get('estado')}''')

def buscar_dispositivo(nombre):
    for dispositivo in datos.inventario:
        if dispositivo.get("nombre") == nombre:
            return dispositivo
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
def eliminar_dispositivo(indice):
    if 0 <= indice < len(datos.inventario):
        eliminado = datos.inventario.pop(indice)
        print(f"Dispositivo '{eliminado.get('nombre')}' eliminado con éxito.")
    else:
        print("Índice fuera de rango. No se pudo eliminar.")


