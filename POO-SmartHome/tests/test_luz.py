import pytest 
from app.dominio.entities.luz import  Luz

def test_luz():
    l = Luz(2, "pieza", False, 0)
    assert l.tipo == "luz"
