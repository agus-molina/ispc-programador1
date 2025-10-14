import mysql.connector
from mysql.connector import errorcode
from app.dao.interfaces.interface_dispositivo_dao import InterfaceDispositivoDAO
from app.dominio.entities.dispositivo import Dispositivo
from app.dominio.entities.luz import Luz
from app.dominio.entities.camara import Camara
from app.dominio.entities.electrodomestico import Electrodomestico
from typing import List, Optional
from app.conn.db_conn import DBConn

class DispositivoDAO(InterfaceDispositivoDAO):

    def __init__(self, db_conn: DBConn):
        self.db_conn=db_conn
        self.db_nombre=db_conn.get_data_base_name()
 
    def get(self, id: int) -> Optional[object]:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "SELECT id_dispositivo, nombre, tipo, estado, intensidad, volumen, infrarrojo FROM dispositivos WHERE id_dispositivo=%s"
                cursor.execute(query, (id,))
                row = cursor.fetchone()
                if row:
                    match row[2]:
                        case "luz":
                            return Luz(row[0], row[1], row[3],row[4])
                        case "camara":
                            return Camara(row[0], row[1], row[3],row[6])
                        case "electrodomestico":
                            return Electrodomestico (row[0], row[1],row[3],row[4],row[5])
                return None
            except mysql.connector.Error as err:
                raise err

    def get_all(self) -> List[object]:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query="SELECT id_dispositivo, nombre, tipo, estado, intensidad, volumen, infrarrojo FROM dispositivos"
                cursor.execute(query)
                rows = cursor.fetchall()
                listaDispositivos = []
                for row in rows:
                    match row[2]:
                        case "luz":
                            listaDispositivos.append(Luz(row[0], row[1], row[3],row[4]))
                        case "camara":
                            listaDispositivos.append(Camara(row[0], row[1], row[3],row[6]))
                        case "electrodomestico":
                            listaDispositivos.append(Electrodomestico (row[0], row[1],row[3],row[4],row[5]))
                return listaDispositivos
            except mysql.connector.Error as err:
                raise err
    
    def create(self, dispositivo: object, id_usuario: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query= "INSERT INTO dispositivos (nombre, tipo, estado, intensidad, volumen, infrarrojo, id_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (dispositivo.nombre, dispositivo.tipo, dispositivo.estado, dispositivo.intensidad, dispositivo.volumen, dispositivo.infrarrojo, id_usuario))
                conn.commit()
                dispositivo.id = cursor.lastrowid
            except mysql.connector.Error as err:
                raise err

    def update(self, dispositivo: object):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                match dispositivo.tipo:
                    case "luz":
                        query="UPDATE dispositivos SET estado=%s, intensidad=%s WHERE id_dispositivo=%s"
                        cursor.execute(query, (dispositivo.estado, dispositivo.intensidad, dispositivo.id))
                    case "camara":
                        query="UPDATE dispositivos SET estado=%s, infrarrojo=%s WHERE id_dispositivo=%s"
                        cursor.execute(query, (dispositivo.estado, dispositivo.infrarrojo, dispositivo.id))
                    case "electrodomestico":
                        query="UPDATE dispositivos SET estado=%s, volumen=%s, intensidad=%s WHERE id_dispositivo=%s"
                        cursor.execute(query, (dispositivo.estado, dispositivo.voumen, dispositivo.intensidad, dispositivo.id))
                conn.commit()
            except mysql.connector.Error as err:
                raise err
    
    def delete(self, id_dispositivo: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query="DELETE FROM dispositivos WHERE id_dispositivo=%s"
                cursor.execute(query, (id_dispositivo,))
                conn.commit()
            except mysql.connector.Error as err:
                raise err