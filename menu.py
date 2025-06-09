'''
MODULO DE PRESENTACION DEL MENU
'''

from admin_dispositivos import (
    listar_dispositivos,
    buscar_dispositivo,
    agregar_dispositivo,
    eliminar_dispositivo,
    ejecutar_automatizacion
)

from usuarios import mostrar_datos_personales
def menu_usuario_estandar(usuario, inventario):
    while True:
        print(f'''\n--- Menú Usuario: {usuario['nombre']} ---
            1. Consultar datos personales")
            2. Ejecutar automatización")
            3. Consultar dispositivos")
            4. Cerrar sesión''')
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            mostrar_datos_personales(usuario)
        elif opcion == "2":
            ejecutar_automatizacion(inventario)
        elif opcion == "3":
            listar_dispositivos(inventario)
        elif opcion == "4":
            print("Cerrando sesión...\n")
            break
        else:
            print("Opción inválida.")