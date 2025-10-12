import mysql.connector
from mysql.connector import errorcode
from app.dao.interfaces.interface_usuario_dao import InterfaceUsuarioDAO
from app.dominio.entities.usuario import Usuario
from typing import List, Optional
from app.conn.db_conn import DBConn

class UsuarioDAO:

    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn.connect_to_mysql()  
        self.db_name = db_conn.get_data_base_name() 

    def get(self, id: int) -> Optional[Usuario]:
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = "SELECT id_usuario, username, contrasena, correo, rol FROM usuarios WHERE id=%s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return Usuario(row[0], row[1], row[2], row[3], row[4])
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all(self) -> List[Usuario]:
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = "SELECT id_usuario, username, contrasena, correo, rol FROM usuarios"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Usuario(row[0], row[1], row[2], row[3], row[4]) for row in rows]
            except mysql.connector.Error as err:
                raise err

    def create(self, usuario: Usuario):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO usuarios (username, contrasena, correo, rol) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (usuario.username, usuario.contrasena, usuario.correo, usuario.rol))
                conn.commit()
                usuario.id = cursor.lastrowid
            except mysql.connector.Error as err:
                raise err

    def update(self, usuario: Usuario):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE usuarios SET username=%s, contrasena=%s, correo=%s, rol=%s WHERE id=%s"
                cursor.execute(query, (usuario.username, usuario.contrasena, usuario.correo, usuario.rol, usuario.id))
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def delete(self, usuario_id: int):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM usuarios WHERE id=%s"
                cursor.execute(query, (usuario_id,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err