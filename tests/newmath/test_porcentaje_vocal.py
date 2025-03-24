import unittest
from tests.base import assert_equal
from newmath.test_porcentaje_vocal import porcentaje_vocales

class TestPorcentajeVocales(unittest.TestCase):

    # Escenario: Valores válidos

    def test_porcentaje_vocales_valido_1(self):
        resultado: float = porcentaje_vocales("Hola, cómo estás?")
        esperado: float = 46.15
        assert_equal(esperado, resultado, "test_porcentaje_vocales_valido_1")

    def test_porcentaje_vocales_valido_2(self):
        resultado: float = porcentaje_vocales("Python")
        esperado: float = 33.33
        assert_equal(esperado, resultado, "test_porcentaje_vocales_valido_2")

    def test_porcentaje_vocales_valido_3(self):
        resultado: float = porcentaje_vocales("AÉÍÓÚ")
        esperado: float = 100.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_valido_3")

    # Escenario: Casos límite

    def test_porcentaje_vocales_limite_1(self):
        resultado: float = porcentaje_vocales("")
        esperado: float = 0.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_limite_1")

    def test_porcentaje_vocales_limite_2(self):
        resultado: float = porcentaje_vocales("12345")
        esperado: float = 0.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_limite_2")

    def test_porcentaje_vocales_limite_3(self):
        resultado: float = porcentaje_vocales("bcdfgh")
        esperado: float = 0.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_limite_3")

    # Escenario: Entradas inválidas
    
    def test_porcentaje_vocales_invalido_1(self):
        with self.assertRaises(TypeError):
            porcentaje_vocales(None)

    def test_porcentaje_vocales_invalido_2(self):
        with self.assertRaises(TypeError):
            porcentaje_vocales(12345)

    def test_porcentaje_vocales_invalido_3(self):
        resultado: float = porcentaje_vocales("!@#$%^&*()")
        esperado: float = 0.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_invalido_3")

    def test_porcentaje_vocales_invalido_4(self):
        resultado: float = porcentaje_vocales("ÁÉÍÓÚáéíóú123")
        esperado: float = 100.0
        assert_equal(esperado, resultado, "test_porcentaje_vocales_invalido_4")

if __name__ == "__main__":
    unittest.main()

