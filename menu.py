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

def menu_admin(usuarios, inventario):
    while True:
        print(f'''\n--- Menú ADMIN ---
            1. Consultar automatizaciones activas
            2. Gestionar dispositivos")
            3. Modificar rol de usuario")
            4. Cerrar sesión\n''')

        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case '1':
                ''' '''
            case '2':
                print(f'''\n--- Gestión de Dispositivos: ---
                1. Listar
                2. Agregar Nuevo
                3. Eliminar
                4. Buscar\n''')

                opcion = input("Seleccione una opción: ").strip()
                match opcion:
                    case 1:
                        listar_dispositivos(inventario)
                    case 2:
                        agregar_dispositivo(inventario, contador_id)
                    case 3:
                        eliminar_dispositivo(inventario)
                    case 4:
                        buscar_dispositivo(inventario, nombre)
                    case _:
                        print("Opción inválida.")
            case '3':
                ''' '''
            case '4':
                print("Cerrando sesión...\n")
                break
            case _:
                print("Opción inválida.")