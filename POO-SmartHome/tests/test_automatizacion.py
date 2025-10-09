import datetime
import pytest
from app.dominio.entities.automatizacion import Automatizacion

@pytest.fixture
def auto():
    hora_on = datetime.time(8, 0, 0)
    hora_off = datetime.time(20, 0, 0)
    return Automatizacion(1, "Luz", False, hora_on, hora_off)

def test_atributos_automatizacion(auto):
    assert auto.id == 1
    assert auto.nombre == "Luz"
    assert auto.estado is False