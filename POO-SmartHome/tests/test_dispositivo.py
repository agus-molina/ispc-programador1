import pytest
from app.dominio.entities.dispositivo import Dispositivo, Luz, Camara, Electrodomestico

def test_encender_apagar():
    d = Dispositivo(1, "Lampara", "luz")
    assert d.estado is False
    d.encender()
    assert d.estado is True
    d.apagar()
    assert d.estado is False



