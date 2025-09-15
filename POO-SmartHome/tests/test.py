import unittest
import datetime
from src.dispositivo import Dispositivo, Luz, Camara, Electrodomestico
from src.usuario import Usuario
from src.automatizacion import Automatizacion

#TEST

class TestAutomatizacion(unittest.TestCase):
    def setUp(self):
        self.hora_on = datetime.time(8, 0, 0)
        self.hora_off = datetime.time(20, 0, 0)
        self.auto = Automatizacion(1, "Luz", False, self.hora_on, self.hora_off)

    def test_atributos(self):
        self.assertEqual(self.auto.id, 1)
        self.assertEqual(self.auto.nombre, "Luz")
        self.assertFalse(self.auto.estado)


class TestDispositivo(unittest.TestCase):
    def test_encender_apagar(self):
        d = Dispositivo( 1, "Lampara", "luz")
        self.assertFalse(d.estado)
        d.encender()
        self.assertTrue(d.estado)
        d.apagar()
        self.assertFalse(d.estado)

    def test_camara(self):
        c = Camara()
        self.assertEqual(c.tipo, "camara")

    def test_luz(self):
        l = Luz()
        self.assertEqual(l.tipo, "luz")

    def test_electrodomestico(self):
        e = Electrodomestico()
        self.assertEqual(e.tipo, "electrodomestico")


class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.user = Usuario(1, "Pepe", "1212", "pepe@mail.com")

    def test_autenticar_correcto(self):
        self.assertTrue(self.user.autenticar("1212"))

    def test_autenticar_incorrecto(self):
        self.assertFalse(self.user.autenticar("abcd"))

    def test_alternar_rol(self):
        self.assertEqual(self.user.rol, "estandar")
        self.user.alternar_rol()
        self.assertEqual(self.user.rol, "admin")
        self.user.alternar_rol()
        self.assertEqual(self.user.rol, "estandar")

    def test_mostrar_datos(self):
        datos = self.user.mostrar_datos()
        self.assertEqual(datos["username"], "Pepe")
        self.assertEqual(datos["rol"], "estandar")


if __name__ == "__main__":
    unittest.main()