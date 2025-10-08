import pytest
from src.usuario import Usuario

@pytest.fixture
def user():
    return Usuario(1, "Pepe", "1212", "pepe@mail.com")

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