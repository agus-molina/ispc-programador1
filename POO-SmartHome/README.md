# POO-SmartHome

Implementación en Python de la Evidencia 5 (POO + TDD).

## Estructura
- `src/` → Clases (`Usuario`, `Dispositivo`, `Automatizacion`)
- `tests/` → Tests unitarios (pytest)

# Evidencia 6 
Este proyecto implementa un sistema modular en Python con arquitectura por capas, que permite la gestión de usuarios, roles y dispositivos, en un sistema con automatizaciones incluidas.

El objetivo es aplicar conceptos de Programación Orientada a Objetos (POO), DAO (Data Access Object) y separación de capas.

# Estructura
POO-SmartHome/
├── app/                                   # Código principal de la aplicación
│   ├── __init__.py                        # Permite tratar la carpeta como paquete Python
│   │
│   ├── conn/                              # Conexión a la base de datos y configuración
│   │   ├── __init__.py
│   │   ├── config.ini                     # Archivo de configuración del entorno o conexión
│   │   └── db_conn.py                     # Módulo que gestiona la conexión a la base de datos
│   │
│   ├── dao/                               # Capa de acceso a datos (Data Access Objects)
│   │   ├── __init__.py
|   |   |   ├── interfaces/
│   |   |       |__        
|   |   |       ├── __init__.py
│   |   |       ├── interface_usuario_dao.py
│   |   |       ├── interface_dispositivo_dao.py
│   |   |       └── interface_automatizacion_dao.py 
│   |   |
│   │   ├── usuario_dao.py                 # DAO para la entidad Usuario
│   │   ├── dispositivo_dao.py             # DAO para la entidad Dispositivo
│   │   └── automatizacion_dao.py          # DAO para las reglas de automatización
│   │
│   ├── dominio/                           # Clases del dominio 
│   │   ├── __init__.py
│   │   ├── usuario.py                     # Clase Usuario y Enum RolUsuario
│   │   ├── dispositivo.py                 # Clase base para dispositivos
│   │   ├── luz.py                         # Clase derivada: Luz 
│   │   ├── electrodomestico.py            # Clase derivada: Electrodoméstico
│   │   ├── camara.py                      # Clase derivada: Cámara de seguridad
│   │   ├── automatizacion.py              # Clase para la lógica de automatización
│   │                      
│   │
│   ├── main.py                            # Punto de entrada de la aplicación
│   └── menu.py                            # Módulo de presentación del menú interactivo
│
├── tests/                                 # Pruebas unitarias del sistema
│   ├── __init__.py
│   ├── test_automatizacion.py
│   ├── test_camara.py
│   ├── test_dispositivo.py
│   ├── test_electrodomestico.py
│   ├── test_luz.py
│   └── test_usuario.py
│
├── README.md                              # Documentación principal del proyecto
├── pytest.ini                             # Configuración del Pytest
├── requirements.txt                       # MYSQL enlace
└── .gitignore                             # Archivos y carpetas ignorados por Git

# Dependencias del proyecto SmartHome
# ----------------------------------
# Este archivo lista los paquetes necesarios para ejecutar el proyecto.
# Se recomienda instalar los requerimientos con:
#     pip install -r requirements.txt

# Conector de base de datos MySQL utilizado por la capa DAO
mysql-connector-python==9.4.0

## Descripción General de Carpetas

- app/ → Contiene toda la lógica principal del sistema, dividida en:

- conn/ → Configuración y conexión a la base de datos.

- dao/ → Clases DAO que manejan el acceso a datos (CRUD).

- dominio/ → Clases del modelo (usuarios, dispositivos, etc.).

- main.py → Punto de entrada del sistema.

- menu.py → Capa de presentación.

- tests/ → Pruebas unitarias organizadas por módulo, ejecutables con pytest.

## Archivos raíz:

- requirements.txt → MYSQL enlace.

- pytest.ini → Configuración de Pytest.

- .gitignore → Archivos a excluir del control de versiones.

- README.md → Documentación general del sistema.

Refactorización y Adaptación a DAO:
Se implementó el patrón DAO (Data Access Object) para aislar la lógica de acceso a datos:
Creación de UsuarioDAO con métodos agregar(), listar(), buscar_por_id(), actualizar() y eliminar().
Integración de la clase DBConn para manejar la conexión a la base de datos MySQL de forma centralizada.

## Modularidad del Proyecto

El proyecto POO-SmartHome fue desarrollado aplicando principios de modularidad, separación de responsabilidades y cohesión interna entre módulos.
Esto significa que cada parte del sistema cumple una función específica, lo que facilita su mantenimiento, reutilización y escalabilidad.

""EN RESUMEN"""

## La modularidad de POO-SmartHome se basa en una arquitectura multicapa que separa de forma clara las responsabilidades:

## Dominio → Qué hace el sistema.

## DAO → Dónde se guardan los datos.

## Conexión → Cómo se accede a los datos.

## Presentación → Cómo interactúa el usuario.

## Tests → Cómo se verifica su correcto funcionamiento.

 ""Conclusión"" 

POO-SmartHome es un sistema modular de gestión de dispositivos inteligentes desarrollado en Python, con arquitectura en capas (Presentación – Dominio – DAO – Conexión – Datos).
Su diseño orientado a objetos facilita la integración de nuevas automatizaciones, sensores y usuarios administradores sin comprometer la estructura actual.

AUTORES:
AGUSTINA MOLINA
MARYSOL RANIERI