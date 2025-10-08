import pytest
from src.dispositivo import Dispositivo, Luz, Camara, Electrodomestico

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

def test_camara_interruptor_infrarrojo():
    c = Camara(1, "frontal", infrarrojo=False)
    assert c._Camara__infrarrojo is False  
    c.interruptor_infrarrojo()
    assert c._Camara__infrarrojo is True  
    c.interruptor_infrarrojo()
    assert c._Camara__infrarrojo is False