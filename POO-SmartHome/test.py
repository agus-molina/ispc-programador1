import unittest
import datetime

#CLASES 

class Automatizacion:
    def __init__(self, id, nombre, estado, hora_activacion, hora_desactivacion):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.hora_activacion = hora_activacion
        self.hora_desactivacion = hora_desactivacion

    def revisar_hora(self):
        hora_actual = datetime.datetime.now().time()
        if self.hora_activacion < self.hora_desactivacion:
            self.estado = self.hora_activacion <= hora_actual < self.hora_desactivacion
        else:
            self.estado = hora_actual >= self.hora_activacion or hora_actual < self.hora_desactivacion


class Dispositivo:
    def __init__(self, id, nombre, tipo, estado=False):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    def encender(self): self.estado = True
    def apagar(self): self.estado = False


class Camara(Dispositivo):
    def __init__(self, id=0, nombre="Camara", tipo="camara"):
        super().__init__(id, nombre, tipo)


class Luz(Dispositivo):
    def __init__(self, id=0, nombre="Luz", tipo="luz"):
        super().__init__(id, nombre, tipo)

    def subir_intensidad(self, cantidad): pass
    def bajar_intensidad(self, cantidad): pass


class Electrodomestico(Dispositivo):
    def __init__(self, id=0, nombre="Electrodomestico", tipo="electrodomestico"):
        super().__init__(id, nombre, tipo)


class Usuario:
    def __init__(self, id, username, contraseña, correo, rol="estandar"):
        self.id = id
        self.username = username
        self.contraseña = contraseña
        self.correo = correo
        self.rol = rol

    def autenticar(self, input_contraseña): return self.contraseña == input_contraseña
    def alternar_rol(self): self.rol = "admin" if self.rol == "estandar" else "estandar"
    def mostrar_datos(self): return {"username": self.username, "rol": self.rol}


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