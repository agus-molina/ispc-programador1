import mysql.connector
from mysql.connector import errorcode
import logging
import configparser
import pathlib


# Configuración del logger
logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.INFO)
# Formateador para los mensajes de registro
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# Manejador para mostrar los registros en la consola
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

class DBConn:
    def __init__(self, config_file="config.ini"):
        self.config_file=config_file
        if (self.config_file!=""):
            # Crear una instancia de ConfigParser
            config=configparser.ConfigParser()
            # Configurar la ruta
            config_path = pathlib.Path(__file__).parent.absolute() / config_file
            # Leer el archivo
            config.read(config_path)
            # Definir una variable db_config que contiene los datos de la sección [database] del archivo.
            self.db_config= config['database']

    def get_data_base_name(self):
        return self.db_config.get('database')

    def connect_to_mysql(self):
        # Conectar a una base de datos MySQL Server
        try:
            return mysql.connector.connect(
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                host=self.db_config.get('host'),
                database=self.db_config.get('database')
            )
        except mysql.connector.Error as err:
            logger.error(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise "Usuario o Password no válido"
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise "La base de datos no existe."
            else:
                raise err
        return None