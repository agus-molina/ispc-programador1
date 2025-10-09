import pytest
from app.dominio.entities.usuario import Usuario

@pytest.fixture
def user():
    return Usuario(1, "Pepe", "1212", "pepe@mail.com")

def test_autenticar_correcto(user):
    assert user.autenticar("1212") is True

def test_autenticar_incorrecto(user):
    assert user.autenticar("abcd") is False

def test_alternar_rol(user):
    assert user.rol._value_ == "estandar"
    user.alternar_rol()
    assert user.rol._value_ == "admin"
    user.alternar_rol()
    assert user.rol._value_ == "estandar"

def test_mostrar_datpyos(user):
    datos = user.mostrar_datos()
    assert datos["username"] == "Pepe"
    assert datos["rol"] == "estandar"