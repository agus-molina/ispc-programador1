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

from EV3.automatizaciones import (
    modo_actual_programa,
    ajuste_automatico
)
from EV3.menu import menu_admin, menu_usuario_estandar
from EV3.usuarios import (
    registrar_usuario,
    login_usuario
)

import EV3.datos as datos


def main():

    print('*** BIENVENIDO AL SISTEMA SMART SOLUTIONS ***')

   
    login = False
    usuario_actual = None

    modo = modo_actual_programa()
    ajuste_automatico(modo)
    print(f'*** El sistema está en modo {modo} ***')

    while True:
        # Flujo por si no hay usuarios registrados
        if not datos.usuarios:
            print("No existen usuarios registrados. Registrá al usuario ADMIN.")
            registrar_usuario(primer_usuario=True)

        # Mientras no haya un usuario logueado, se solicita iniciar sesión o registrar un usuario estándar
        while not usuario_actual:
            try:
                print("\n1. Iniciar sesión\n2. Registrar usuario estándar")
                opcion = int(input("Seleccione una opción: ").strip())
                match opcion:
                    case 1:
                        usuario_actual = login_usuario()
                        if usuario_actual:
                            login = True
                    case 2:
                        registrar_usuario()
                    case _:
                        print("Opción inválida.")
            except ValueError:
                print("Opción inválida.")

    # Menú segun rol
        while login:
            try:
                if usuario_actual["rol"] == "admin":
                    accion = menu_admin(modo)
                else:
                    accion = menu_usuario_estandar(usuario_actual, modo)
                if accion == "logout":
                    usuario_actual = None  # sale de la sesíon
                    login = False          # vuelve al menú de inicio
                elif accion == "exit":
                    print("Programa finalizado. ¡Gracias por usar Smart Solutions!")
                    return # sale del programa
            except ValueError:
                print("Opción inválida.\n")

if __name__ == "__main__":
    main()