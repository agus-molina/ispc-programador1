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
from datos import inventario, usuarios

def menu_usuario_estandar(usuario, modo):

    print(f'''\n--- Menú Usuario: {usuario['nombre']} ---
        1. Consultar datos personales
        2. Ejecutar automatización
        3. Consultar dispositivos
        4. Cerrar sesión''')
    
    opcion = int(input("Seleccione una opción: ").strip())
    match opcion:
        case 1:
            mostrar_datos_personales(usuario)
            return True
        case 2:
            ajuste_automatico(modo)
            return True
        case 3:
            listar_dispositivos()
            return True
        case 4:
            print("Cerrando sesión...\n")
            return False
        case _:
            print("Opción inválida.")
            return True

def menu_admin(modo):

    print(f'''\n--- Menú ADMIN ---
        1. Consultar automatizaciones activas
        2. Gestionar dispositivos
        3. Modificar rol de usuario
        4. Cerrar sesión\n''')

    opcion = int(input("Seleccione una opción: ").strip())
    match opcion:
        case 1:
            print(f'El sistema esta en modo {modo}!')
            return True
        case 2:
            print(f'''\n--- Gestión de Dispositivos: ---
            1. Listar
            2. Agregar Nuevo
            3. Eliminar
            4. Buscar\n''')

            opcion = int(input("Seleccione una opción: ").strip())
            match opcion:
                case 1:
                    listar_dispositivos()
                    return True
                case 2:
                    agregar_dispositivo()
                    ajuste_automatico(modo)
                    return True
                case 3:
                    listar_dispositivos()
                    dispositivo = int(input("Ingrese el ID del dispositivo por eliminar: ").strip())
                    eliminar_dispositivo(dispositivo)
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
            return False
        case _:
            print("Opción inválida.")
            return True