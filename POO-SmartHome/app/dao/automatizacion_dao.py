import mysql.connector
from mysql.connector import errorcode
from app.dao.interfaces.interface_automatizacion_dao import InterfaceAutomatizacionDAO
from app.dominio.entities.automatizacion import Automatizacion
from typing import List, Optional
from app.conn.db_conn import DBConn

class AutomatizacionDAO:

    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn  
        self.db_name = db_conn.get_data_base_name() 

    def get(self, id: int) -> Optional[Automatizacion]:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "SELECT id_automatizacion, nombre, estado, hora_activacion, hora_desactivacion FROM automatizaciones WHERE id_automatizacion=%s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    return Automatizacion(row[0],row[1],row[2],row[3],row[4])
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all(self) -> List[Automatizacion]:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "SELECT id_automatizacion, nombre, estado, hora_activacion, hora_desactivacion FROM automatizaciones"
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Automatizacion(row[0], row[1], row[2], row[3], row[4]) for row in rows]
            except mysql.connector.Error as err:
                raise err

    def create(self, automatizacion: Automatizacion, id_usuario: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO automatizaciones (nombre, estado, hora_activacion, hora_desactivacion, id_usuario) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (automatizacion.nombre, automatizacion.estado, automatizacion.hora_activacion, automatizacion.hora_desactivacion, id_usuario))
                conn.commit()
                automatizacion.id = cursor.lastrowid
            except mysql.connector.Error as err:
                raise err

    def update(self, automatizacion: Automatizacion):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE automatizaciones SET estado=%s WHERE id_automatizacion=%s"
                cursor.execute(query, (automatizacion.estado, automatizacion.id))
                conn.commit()
            except mysql.connector.Error as err:
                raise err

    def delete(self, automatizacion_id: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM automatizaciones WHERE id_automatizacion=%s"
                cursor.execute(query, (automatizacion_id,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err