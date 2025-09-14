'''
MODULO CON PROPIEDADES EN COMUN PARA TODOS LOS USUARIOS
'''

import EV3.datos as datos

# Cuando no existe el usuario lo registra /NO TIENE VALIDACIONES O LIMITE DE CARACTERES
def registrar_usuario(primer_usuario=False):
    print("\n*** Registro de Usuario ***")
    nombre = input("Nombre completo: ").strip()
    username = input("Nombre de usuario: ").strip()
    password = input("Contraseña: ").strip()
    rol = 'admin' if primer_usuario else 'estandar'

    # Verificar que el usuario no exista
    for user in datos.usuarios:
        if user['username'] == username:
            print("Ya existe un usuario con ese nombre de usuario.")
            return False

    datos.usuarios.append({
        'nombre': nombre,
        'username': username,
        'password': password,
        'rol': rol
    })
    print(f"Usuario {'Admin' if rol == 'admin' else 'Estándar'} registrado con éxito.")
    return True

# Login sencillo sin validaciones o limites
def login_usuario():
    print("\n*** Iniciar Sesión ***")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    for user in datos.usuarios:
        if user['username'] == username and user['password'] == password:
            print(f"Bienvenido, {user['nombre']}! Rol: {user['rol']}")
            return user
    print("Usuario o contraseña incorrectos.")
    return None

def mostrar_datos_personales(usuario):
    print(f'''\n
        --- Datos Personales ---
        Nombre: {usuario['nombre']}
        Usuario: {usuario['username']}
        Rol: {usuario['rol']}''')

# cambia rol a admin pero no avisa si el usuario elegido no existe
def cambiar_rol(eleccion):
    for usuario in datos.usuarios:
        if eleccion == usuario["nombre"] or eleccion == usuario["username"]:
            usuario["rol"] = "admin"
            print(f"Rol de {usuario['nombre']}  cambiado exitosamente!")
            return True
    print("No se encontró un usuario con ese nombre o username.")
    return False