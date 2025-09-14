import pytest
from src.dispositivo import Dispositivo
from src.automatizacion import Automatizacion

def test_automatizacion_noche():
    d1 = Dispositivo(1, "Lámpara", "luces")
    d2 = Dispositivo(2, "Cámara", "camara")
    auto = Automatizacion("NOCHE")
    resultados = auto.ajustar_dispositivos([d1, d2])

    assert d1.estado is False
    assert d2.estado is True
    assert any("apagado" in r or "encendida" in r for r in resultados)

