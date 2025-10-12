import mysql.connector
from mysql.connector import errorcode
from app.dao.interfaces.interface_dispositivo_dao import InterfaceDispositivoDAO
from app.dominio.entities.dispositivo import Dispositivo
from typing import List, Optional
from app.conn.db_conn import DBConn

class DispositivoDAO(InterfaceDispositivoDAO):

    def __init__(self, db_conn: DBConn):
        self.db_conn=db_conn.connect_to_mysql()
        self.db_nombre=db_conn.get_data_base_name()
 
    def get(self, id: int) -> Optional[Dispositivo]:
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_dispositivo, nombre, tipo, estado, intensidad, volumen, infrarrojo FROM dispositivos WHERE id=%s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return Dispositivo(row[0], row[1], row[2], row[3], row[4], row[5],row[6])
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all(self) -> List[Dispositivo]:
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query="SELECT id_dispositivo, nombre, tipo, estado, intensidad, volumen, infrarrojo FROM dispositivos"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Dispositivo(row[0], row[1], row[2], row[3], row[4], row[5],row[6]) for row in rows]
            except mysql.connector.Error as err:
                raise err
    
    def create(self, dispositivo: Dispositivo, id_usuario: int):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query= "INSERT INTO dispositivos (nombre, tipo, estado, intensidad, volumen, infrarrojo, id_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (dispositivo.nombre, dispositivo.tipo, dispositivo.estado, dispositivo.intensidad, dispositivo.volumen, dispositivo.infrarrojo, id_usuario))
                conn.commit()
                dispositivo.id = cursor.lastrowid
            except mysql.connector.Error as err:
                raise err

    def update(self, dispositivo: Dispositivo):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query="UPDATE dispositivos SET nombre=%s, estado=%s, intensidad=%s, volumen=%s, infrarrojo=%s WHERE id=%s"
                cursor.execute(query, (dispositivo.nombre, dispositivo.estado, dispositivo.intensidad, dispositivo.volumen, dispositivo.infrarrojo, dispositivo.id))
                conn.commit()
            except mysql.connector.Error as err:
                raise err
    
    def delete(self, id_dispositivo: int):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query="DELETE FROM dispositivos WHERE id_dispositivo=%s"
                cursor.execute(query, (id_dispositivo,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err
