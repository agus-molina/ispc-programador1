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

    tipos_validos = {"electrodomestico", "luces", "camara", "luz"}  # admito singular y plural
    if tipo not in tipos_validos:
        print("Tipo inválido. Use ELECTRODOMESTICO / LUCES / CAMARA.")
        return

    def leer_numero_en_rango(prompt, minimo=0, maximo=100):
        txt = input(prompt).strip()
        if not txt.isdigit():
            print("Valor inválido. Debe ser numérico.")
            return None
        n = int(txt)
        if n < minimo or n > maximo:
            print(f"Valor fuera de rango ({minimo}–{maximo}).")
            return None
        return n
    estado_txt = input('¿Está encendido? (s/n): ').strip().lower()
    estado = estado_txt in ("s", "si", "sí", "y", "yes")

    dispositivo = {
        "id": datos.contador_id,
        "nombre": nombre,
        "tipo": "luz" if tipo == "luces" else tipo,  # normalizo a singular
        "estado": estado
    }
    if tipo in ("luces", "luz", "electrodomestico"):
        intensidad = leer_numero_en_rango("Intensidad (0-100): ")
        if intensidad is None:
            return
        dispositivo["intensidad"] = intensidad

    if tipo == "electrodomestico":
        volumen = leer_numero_en_rango("Volumen (0-100): ")
        if volumen is None:
            return
        dispositivo["volumen"] = volumen
    if tipo == "camara":
        ir_txt = input('¿Infrarrojo activado? (s/n): ').strip().lower()
        dispositivo["infrarrojo"] = ir_txt in ("s", "si", "sí", "y", "yes")

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