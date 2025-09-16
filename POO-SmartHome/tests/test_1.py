import datetime
import pytest
from src.dispositivo import Dispositivo, Luz, Camara, Electrodomestico
from src.usuario import Usuario
from src.automatizacion import Automatizacion


# ---------- FIXTURES ----------

@pytest.fixture
def auto():
    hora_on = datetime.time(8, 0, 0)
    hora_off = datetime.time(20, 0, 0)
    return Automatizacion(1, "Luz", False, hora_on, hora_off)

@pytest.fixture
def user():
    return Usuario(1, "Pepe", "1212", "pepe@mail.com")


# ---------- TEST Automatizacion ----------

def test_atributos_automatizacion(auto):
    assert auto.id == 1
    assert auto.nombre == "Luz"
    assert auto.estado is False


# ---------- TEST Dispositivo ----------

def test_encender_apagar():
    d = Dispositivo(1, "Lampara", "luz")
    assert d.estado is False
    d.encender()
    assert d.estado is True
    d.apagar()
    assert d.estado is False

def test_camara():
    c = Camara(1, "frontal")
    assert c.tipo == "camara"

def test_luz():
    l = Luz(2, "pieza")
    assert l.tipo == "luz"

def test_electrodomestico():
    e = Electrodomestico(3, "tele")
    assert e.tipo == "electrodomestico"


# ---------- TEST Usuario ----------

def test_autenticar_correcto(user):
    assert user.autenticar("1212") is True

def test_autenticar_incorrecto(user):
    assert user.autenticar("abcd") is False

def test_alternar_rol(user):
    assert user.rol == "estandar"
    user.alternar_rol()
    assert user.rol == "admin"
    user.alternar_rol()
    assert user.rol == "estandar"

def test_mostrar_datos(user):
    datos = user.mostrar_datos()
    assert datos["username"] == "Pepe"
    assert datos["rol"] == "estandar"