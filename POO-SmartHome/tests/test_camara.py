import pytest 
from app.dominio.entities.camara import Camara

def test_camara():
    c = Camara(1, "frontal", False, False)
    assert c.tipo == "camara"

def test_camara_interruptor_infrarrojo():
    c = Camara(1, "frontal", False, False)
    assert c.infrarrojo is False  
    c.interruptor_infrarrojo()
    assert c.infrarrojo is True  
    c.interruptor_infrarrojo()
    assert c.infrarrojo is False