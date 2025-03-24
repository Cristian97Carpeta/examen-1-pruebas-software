import unittest
from tests.base import assert_equal
from newmath.test_multiplicar_vocales import multiplicacion_vocales

class TestMultiplicacionVocales(unittest.TestCase):

    # Escenario: Valores válidos
    
    def test_multiplicacion_vocales_valido_1(self):
        resultado: int = multiplicacion_vocales("aeiou")
        esperado: int = 9
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_valido_1")

    def test_multiplicacion_vocales_valido_2(self):
        resultado: int = multiplicacion_vocales("AEIOU")
        esperado: int = -5
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_valido_2")

    def test_multiplicacion_vocales_valido_3(self):
        resultado: int = multiplicacion_vocales("áéíóú")
        esperado: int = 20
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_valido_3")

    # Escenario: Casos límite

    def test_multiplicacion_vocales_limite_1(self):
        resultado: int = multiplicacion_vocales("")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_limite_1")

    def test_multiplicacion_vocales_limite_2(self):
        resultado: int = multiplicacion_vocales("aaaaaaa")
        esperado: int = 21
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_limite_2")

    def test_multiplicacion_vocales_limite_3(self):
        resultado: int = multiplicacion_vocales("ÁÁÁÁ")
        esperado: int = 16
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_limite_3")

    # Escenario: Entradas inválidas

    def test_multiplicacion_vocales_invalido_1(self):
        with self.assertRaises(TypeError):
            multiplicacion_vocales(None)

    def test_multiplicacion_vocales_invalido_2(self):
        with self.assertRaises(TypeError):
            multiplicacion_vocales(12345)

    def test_multiplicacion_vocales_invalido_3(self):
        resultado: int = multiplicacion_vocales("12345")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_invalido_3")

    def test_multiplicacion_vocales_invalido_4(self):
        resultado: int = multiplicacion_vocales("!@#$%^&*()")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_multiplicacion_vocales_invalido_4")
