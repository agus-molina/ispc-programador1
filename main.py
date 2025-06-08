'''  Actividad Integradora N° 3
Programación I
Permitir el registro de un nuevo usuario estándar e inicio de sesión.
Si el usuario estándar inició sesión satisfactoriamente, permitir las siguientes acciones mediante un menú:
Permitir consultar los datos personales.
Permitir activar/ejecutar/”configurar”(debería estar predefinida) la automatización.
Permitir consultar dispositivos.
Si el usuario admin inició sesión satisfactoriamente, permitir las siguientes acciones mediante un menú:
Permitir consultar automatizaciones activas
Gestionar dispositivos.
Permitir modificar el rol de un usuario. 

** El usuario Admin, puede ser el primer usuario que se registra.**
 '''

from funciones import (
    modo_actual_programa,
    mostrar_menu,
    listar_dispositivos,
    buscar_dispositivo,
    agregar_dispositivo,
    eliminar_dispositivo,
    ajuste_automatico
)

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
        try:
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
                        id_a_eliminar = int(input('Ingrese la ID del dispositivo a Desvincular: ').strip())
                        eliminado = eliminar_dispositivo(inventario, id_a_eliminar)
                        if eliminado:
                            print(f'Dispositivo con ID {id_a_eliminar} eliminado correctamente.')
                        else:
                            print(f'No se encontró un dispositivo con ID {id_a_eliminar}.')
                case 5:
                    print('Muchas gracias por utilizar Smart Solutions...')
                    print('Saliendo del sistema...')
                    login = False
                case _:
                    print("Opción inválida. Por favor, ingrese un número que corresponda\n")
        except ValueError:
            print("Opción inválida.\n")

if __name__ == "__main__":
    main()