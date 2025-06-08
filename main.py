'''  Actividad Integradora N° 2
Programación I
Basándose en los requerimientos funcionales y no funcionales del proyecto, se
solicita inicialmente:
1. Realizar un programa modular que cumpla con los requerimientos generales
del programa que son:
a. Gestionar los dispositivos (listar, buscar, agregar y eliminar)
b. Gestionar automatizaciones (sólo una).
Nota: Almacenar la información en estructuras de datos (ej. listas,
diccionarios) '''

from funciones import *

def main():
    print('*** BIENVENIDO AL SISTEMA SMART SOLUTIONS ***')

    inventario = []
    contador_id = 0
    login = True

    modo = modo_actual_programa()
    ajuste_automatico(inventario, modo)
    print(f'*** El sistema está en modo {modo} ***')

    while login:
        mostrar_menu()
        seleccion_valida = False
        while not seleccion_valida:
            entrada = input("Seleccione el número de la opción deseada: ").strip()
            if entrada.isdigit():
                seleccion = int(entrada)
                seleccion_valida = True
            else:
                print("Entrada inválida. Por favor, ingrese un número correspondiente a las opciones del menú.\n")

        seleccion = int(input("Seleccione el número de la opción deseada: ").strip())
        match seleccion:
            case 1:
                listar_dispositivos(inventario)
            case 2:
                busqueda = input('Ingresa el "NOMBRE" del Dispositivo a buscar: ').strip().lower()
                resultado = buscar_dispositivo(inventario, busqueda)
                if resultado:
                    print('Dispositivo Encontrado:')
                    print(f'''ID: {resultado.get('id')}
                    Nombre: {resultado.get('nombre')}
                    Tipo: {resultado.get('tipo')}
                    Estado: {resultado.get('estado')}''')
                else:
                    print('Dispositivo no encontrado...')
            case 3:
                agregar_dispositivo(inventario, contador_id)
                contador_id += 1
            case 4:
                if inventario:
                    print("\n*** Dispositivos disponibles para eliminar ***")
                    for dispositivo in inventario:
                        print(f"ID: {dispositivo.get('id')} - Nombre: {dispositivo.get('nombre')}")
                    try:
                        id_a_eliminar = int(input('Ingrese la ID del dispositivo a Desvincular: ').strip())
                        eliminado = eliminar_dispositivo(inventario, id_a_eliminar)
                        if eliminado:
                            print(f'Dispositivo con ID {id_a_eliminar} eliminado correctamente.')
                        else:
                            print(f'No se encontró un dispositivo con ID {id_a_eliminar}.')
                    except ValueError:
                        print('Por favor, ingrese un número válido para la ID.')
            case 5:
                print('Muchas gracias por utilizar Smart Solutions...')
                print('Saliendo del sistema...')
                login = False
            case _:
                print("Entrada inválida. Por favor, ingrese un número que corresponda\n")

if __name__ == "__main__":
    main()