import unittest
from tests.base import assert_equal
from newmath.string import contar_vocales, multiplicacion_vocales, porcentaje_vocales

class TestContarVocales(unittest.TestCase):

    # Escenario: Valores válidos

    def test_contar_vocales_valido_1(self):
        resultado: int = contar_vocales("Hola, cómo estás?")
        esperado: int = 7
        assert_equal(esperado, resultado, "test_contar_vocales_valido_1")

    def test_contar_vocales_valido_2(self):
        resultado: int = contar_vocales("AEIOUaeiouÁÉÍÓÚáéíóú")
        esperado: int = 20
        assert_equal(esperado, resultado, "test_contar_vocales_valido_2")

    def test_contar_vocales_valido_3(self):
        resultado: int = contar_vocales("Esta es una prueba sin acentos.")
        esperado: int = 11
        assert_equal(esperado, resultado, "test_contar_vocales_valido_3")

    # Escenario: Casos límite

    def test_contar_vocales_limite_1(self):
        resultado: int = contar_vocales("")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_contar_vocales_limite_1")

    def test_contar_vocales_limite_2(self):
        resultado: int = contar_vocales("aaaaa")
        esperado: int = 5
        assert_equal(esperado, resultado, "test_contar_vocales_limite_2")

    def test_contar_vocales_limite_3(self):
        resultado: int = contar_vocales("áéíóúÁÉÓÍÚ")
        esperado: int = 10
        assert_equal(esperado, resultado, "test_contar_vocales_limite_3")

    # Escenario: Entradas inválidas
    
    def test_contar_vocales_invalido_1(self):
        with self.assertRaises(TypeError):
            contar_vocales(None)

    def test_contar_vocales_invalido_2(self):
        with self.assertRaises(TypeError):
            contar_vocales(12345)

    def test_contar_vocales_invalido_3(self):
        resultado: int = contar_vocales("12345")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_contar_vocales_invalido_3")

    def test_contar_vocales_invalido_4(self):
        resultado: int = contar_vocales("!@#$%^&*()")
        esperado: int = 0
        assert_equal(esperado, resultado, "test_contar_vocales_invalido_4")

if __name__ == "__main__":
    unittest.main()





