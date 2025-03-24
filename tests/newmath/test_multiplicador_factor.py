import unittest
from tests.base import assert_equal
from newmath.factor import multiplicador_factor

class TestMultiplicadorFactor(unittest.TestCase):

    # Escenario: Valores válidos

    def test_multiplicador_factor_valido_1(self):
        resultado: float = multiplicador_factor(5, -3, 15)
        esperado: float = 58.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_valido_1")

    def test_multiplicador_factor_valido_2(self):
        resultado: float = multiplicador_factor(-3, 5, 15)
        esperado: float = 58.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_valido_2")

    def test_multiplicador_factor_valido_3(self):
        resultado: float = multiplicador_factor(10, 2, 20)
        esperado: float = 45.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_valido_3")

    # Escenario: Casos límite

    def test_multiplicador_factor_limite_1(self):
        resultado: float = multiplicador_factor(0, 2, 10)
        esperado: float = 10.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_limite_1")

    def test_multiplicador_factor_limite_2(self):
        resultado: float = multiplicador_factor(1000, -1000, 1)
        esperado: float = 0.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_limite_2")

    def test_multiplicador_factor_limite_3(self):
        resultado: float = multiplicador_factor(-1, -1, -1)
        esperado: float = -1.0
        assert_equal(esperado, resultado, "test_multiplicador_factor_limite_3")

    # Escenario: Entradas inválidas

    def test_multiplicador_factor_invalido_1(self):
        with self.assertRaises(TypeError):
            multiplicador_factor("cinco", 2, 3)

    def test_multiplicador_factor_invalido_2(self):
        with self.assertRaises(TypeError):
            multiplicador_factor(5, None, 15)

    def test_multiplicador_factor_invalido_3(self):
        with self.assertRaises(ValueError):
            multiplicador_factor(5, 2, -100)

    def test_multiplicador_factor_invalido_4(self):
        with self.assertRaises(ValueError):
            multiplicador_factor(-5, 0, 0)

if __name__ == "__main__":
    unittest.main()

