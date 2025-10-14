"""
Main hecho como prueba para verificar que los objetos dao interactuan con la base de datos
"""


from app.dao.usuario_dao import UsuarioDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.dao.automatizacion_dao import AutomatizacionDAO
from app.dominio.entities.usuario import Usuario, RolUsuario
from app.dominio.entities.dispositivo import Dispositivo
from app.dominio.entities.luz import Luz
from app.dominio.entities.camara import Camara
from app.dominio.entities.electrodomestico import Electrodomestico
from app.dominio.entities.automatizacion import Automatizacion
from app.conn.db_conn import DBConn

def main():

    # Conexión
    db_conn = DBConn()

    # DAOs
    usuario_dao = UsuarioDAO(db_conn)
    dispositivo_dao = DispositivoDAO(db_conn)
    automatizacion_dao = AutomatizacionDAO(db_conn)

    # Usuarios
    
    print("=== USUARIOS ===")
    # Crear
    u1 = Usuario(id=None, username="María", contrasena="123", correo="maria@example.com", rol=RolUsuario.ADMIN)
    u2 = Usuario(id=None, username="Nahuel", contrasena= "1234", correo="nahuel@example.com", rol=RolUsuario.ESTANDAR)
    usuario_dao.create(u1)
    usuario_dao.create(u2)

    # Listar
    usuarios = usuario_dao.get_all()
    print("Usuarios actuales:")
    for u in usuarios:
        print(f"ID:{u.id}, Nombre:{u.username}, correo:{u.correo}, Rol:{u.rol}")

    # Buscar
    u = usuario_dao.get(1)
    if u:
        print(f"\nUsuario con ID 1: {u.username}, {u.correo}, {u.rol}")

    # Actualizar
    if u:
        u.alternar_rol()
        usuario_dao.update(u)
        print("\nDespués de actualizar:")
        for u in usuario_dao.get_all():
            print(f"ID:{u.id}, Nombre:{u.username}, correo:{u.correo}, Rol:{u.rol}")

    # Eliminar
    usuario_dao.delete(2)
    print("\nDespués de eliminar usuario con ID 2:")
    for u in usuario_dao.get_all():
        print(f"ID:{u.id}, Nombre:{u.username}, correo:{u.correo}, Rol:{u.rol}")

    # Dispositivos
   
    print("\n=== DISPOSITIVOS ===")
    # Crear
    d1 = Luz(id=None, nombre="lamparita", estado=False, intensidad=0)
    d2 = Camara(id=None, nombre="camarita", estado=False, infrarrojo=False)
    print(f"ID:{d1.id}, Name:{d1.nombre}, Tipo: {d1.tipo}, Estado: {d1.estado}, Intensidad: {d1.intensidad}, Volumen: {d1.volumen}, Infrarrojo: {d1.infrarrojo}")
    print(f"ID:{d2.id}, Name:{d2.nombre}, Tipo: {d2.tipo}, Estado: {d2.estado}, Intensidad: {d2.intensidad}, Volumen: {d2.volumen}, Infrarrojo: {d2.infrarrojo}")
    dispositivo_dao.create(d1, 1)
    dispositivo_dao.create(d2, 1)

    # Listar
    dispositivos = dispositivo_dao.get_all()
    print("Dispositivos actuales:")
    for d in dispositivos:
        print(f"ID:{d.id}, Name:{d.nombre}, Tipo: {d.tipo}, Estado: {d.estado}, Intensidad: {d.intensidad}, Volumen: {d.volumen}, Infrarojo: {d.infrarrojo}")

    # Actualizar
    d = dispositivo_dao.get(1)
    if d:
        d.subir_intensidad(30)
        dispositivo_dao.update(d)
        print("\nDespués de actualizar:")
        for d in dispositivo_dao.get_all():
            print(f"ID:{d.id}, Name:{d.nombre}, Tipo: {d.tipo}, Estado: {d.estado}, Intensidad: {d.intensidad}, Volumen: {d.volumen}, Infrarojo: {d.infrarrojo}")

    # Eliminar
    dispositivo_dao.delete(2)
    print("\nDespués de eliminar dispositivo con ID 2:")
    for d in dispositivo_dao.get_all():
        print(f"ID:{d.id}, Name:{d.nombre}, Tipo: {d.tipo}, Estado: {d.estado}, Intensidad: {d.intensidad}, Volumen: {d.volumen}, Infrarojo: {d.infrarrojo}")

    print("=== AUTOMATIZACIONES ===")
    #Crear
    a1= Automatizacion(id=None, nombre="aut1", estado=False, hora_activacion="23:59:59", hora_desactivacion="06:00:00")
    a2= Automatizacion(id=None, nombre="aut2", estado=False, hora_activacion="22:00:00", hora_desactivacion="06:00:00")
    automatizacion_dao.create(a1, 1)
    automatizacion_dao.create(a2, 1)
    #Listar
    automatizaciones = automatizacion_dao.get_all()
    print("automatizaciones actuales:")
    for a in automatizaciones:
        print(f"ID:{a.id}, Name:{a.nombre}, Estado: {a.estado}, hora_activacion: {a.hora_activacion}, hora_desactivacion: {a.hora_desactivacion}")

    # Actualizar
    a = automatizacion_dao.get(1)
    if a:
        a.activar()
        automatizacion_dao.update(a)
        print("\nDespués de actualizar:")
        for a in automatizacion_dao.get_all():
            print(f"ID:{a.id}, Name:{a.nombre}, Estado: {a.estado}, hora_activacion: {a.hora_activacion}, hora_desactivacion: {a.hora_desactivacion}")

    # Eliminar
    automatizacion_dao.delete(2)
    print("\nDespués de eliminar dispositivo con ID 2:")
    for a in automatizacion_dao.get_all():
        print(f"ID:{a.id}, Name:{a.nombre}, Estado: {a.estado}, hora_activacion: {a.hora_activacion}, hora_desactivacion: {a.hora_desactivacion}")


if __name__ == "__main__":
    main()


