import pytest
from src.usuario import Usuario

def test_crear_usuario():
    u = Usuario("Juan Pérez", "juanp", "1234")
    datos = u.mostrar_datos()
    assert datos["nombre"] == "Juan Pérez"
    assert datos["rol"] == "estandar"

def test_cambiar_rol():
    u = Usuario("Admin", "admin", "1234")
    u.cambiar_rol("admin")
    assert u.rol == "admin"
