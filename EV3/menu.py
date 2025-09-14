'''
MODULO DE PRESENTACION DEL MENU
'''

from admin_dispositivos import (
    listar_dispositivos,
    buscar_dispositivo,
    agregar_dispositivo,
    eliminar_dispositivo
)
from automatizaciones import ajuste_automatico
from usuarios import mostrar_datos_personales, cambiar_rol

def menu_usuario_estandar(usuario, modo, inventario):

    print(f'''\n--- Menú Usuario: {usuario['nombre']} ---
        1. Consultar datos personales
        2. Ejecutar automatización
        3. Consultar dispositivos
        4. Cerrar sesión
        5. Salir del sistema
        ''')
    
    opcion_txt = input("Seleccione una opción: ").strip()
    if not opcion_txt.isdigit():
        print("Opción inválida.")
        return True
    opcion = int(opcion_txt)
    match opcion:
        case 1:
            mostrar_datos_personales(usuario)
            return True
        case 2:
            resultados = ajuste_automatico(modo)
            print("\nResultados de la automatización:")
            if resultados:
                for r in resultados:
                    print("-", r)
            else: 
                print("No hay dispositivos para automatizar")
            return True
        case 3:
            listar_dispositivos()
            return True
        case 4:
            print("Cerrando sesión...\n")
            return "logout"
        case 5:
            print("Saliendo del sistema...\n")
            return "exit"
        case _:
            print("Opción inválida.")
            return True

def menu_admin(modo):

    print(f'''\n--- Menú ADMIN ---
        1. Consultar automatizaciones activas
        2. Gestionar dispositivos
        3. Modificar rol de usuario
        4. Cerrar sesión
        5. Salir del sistema\n''')

    opcion_txt = input("Seleccione una opción: ").strip()
    if not opcion_txt.isdigit():
        print("Opción inválida.")
        return True
    opcion = int(opcion_txt)
    match opcion:
        case 1:
            print(f'El sistema esta en modo {modo}!')
            listar_dispositivos()
            return True
        case 2:
            print(f'''\n--- Gestión de Dispositivos: ---
            1. Listar
            2. Agregar Nuevo
            3. Eliminar
            4. Buscar\n''')

            subop_txt = input("Seleccione una opción: ").strip()
            if not subop_txt.isdigit():
                print("Opción inválida.")
                return True
            subop = int(subop_txt)

            match subop:
                case 1:
                    listar_dispositivos()
                    return True
                case 2:
                    agregar_dispositivo()
                    ajuste_automatico(modo)
                    return True
                case 3:
                    listar_dispositivos()
                    id_txt = input("Ingrese el ID del dispositivo por eliminar: ").strip()
                    if not id_txt.isdigit():
                        print("ID inválido.")
                        return True
                    dispositivo_id = int(id_txt)
                    eliminar_dispositivo(dispositivo_id)
                    return True
                case 4:
                    nombre = input("Ingresa el nombre del dispositivo: ").strip()
                    buscar_dispositivo(nombre)
                    return True
                case _:
                    print("Opción inválida.")
                    return True
        case 3:
            eleccion = input("Indique el nombre del usuario a modificar: ").strip()
            cambiar_rol(eleccion)
            return True
        case 4:
            print("Cerrando sesión...\n")
            return "logout"
        case 5:
            print("Saliendo del sistema...\n")
            return "exit"

        case _:
            print("Opción inválida.")
            return True