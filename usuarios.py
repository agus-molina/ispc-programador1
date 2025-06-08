'''
MODULO CON PROPIEDADES EN COMUN PARA TODOS LOS USUARIOS
'''

def registrar_usuario(usuarios, primer_usuario=False):
    print("\n*** Registro de Usuario ***")
    nombre = input("Nombre completo: ").strip()
    username = input("Nombre de usuario: ").strip()
    password = input("Contraseña: ").strip()
    rol = 'admin' if primer_usuario else 'estandar'

    # Verificar que el usuario no exista
    for user in usuarios:
        if user['username'] == username:
            print("Ya existe un usuario con ese nombre de usuario.")
            return False

    usuarios.append({
        'nombre': nombre,
        'username': username,
        'password': password,
        'rol': rol
    })
    print(f"Usuario {'Admin' if rol == 'admin' else 'Estándar'} registrado con éxito.")
    return True

def login_usuario(usuarios):
    print("\n*** Iniciar Sesión ***")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    for user in usuarios:
        if user['username'] == username and user['password'] == password:
            print(f"Bienvenido, {user['nombre']}! Rol: {user['rol']}")
            return user
    print("Usuario o contraseña incorrectos.")
    return None