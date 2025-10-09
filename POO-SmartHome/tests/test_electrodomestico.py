import pytest 
from app.dominio.entities.electrodomestico import Electrodomestico


def test_electrodomestico():
    e = Electrodomestico(3, "tele")
    assert e.tipo == "electrodomestico"
