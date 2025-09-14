import pytest
from src.dispositivo import Dispositivo

def test_encender_y_apagar():
    d = Dispositivo(1, "Lámpara", "luces")
    d.encender()
    assert d.estado is True
    d.apagar()
    assert d.estado is False
