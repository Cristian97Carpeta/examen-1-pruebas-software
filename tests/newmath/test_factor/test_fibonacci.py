import unittest
from tests.base import assert_equal
from newmath.factor import factor_fibonacci

class TestFactorFibonacci(unittest.TestCase):

    # Escenario: Valores válidos

    def test_factor_fibonacci_valido_1(self):
        resultado: float = factor_fibonacci(5)
        esperado: float = 1.0
        assert_equal(esperado, resultado, "test_factor_fibonacci_valido_1")

    def test_factor_fibonacci_valido_2(self):
        resultado: float = factor_fibonacci(6, 2, 3)
        esperado: float = 5.67
        assert_equal(esperado, resultado, "test_factor_fibonacci_valido_2")

    def test_factor_fibonacci_valido_3(self):
        resultado: float = factor_fibonacci(10, 0, 1)
        esperado: float = 11.0
        assert_equal(esperado, resultado, "test_factor_fibonacci_valido_3")

    # Escenario: Casos límite

    def test_factor_fibonacci_limite_1(self):
        resultado: float = factor_fibonacci(1)
        esperado: float = 1.0
        assert_equal(esperado, resultado, "test_factor_fibonacci_limite_1")

    def test_factor_fibonacci_limite_2(self):
        resultado: float = factor_fibonacci(2, -2, -1)
        esperado: float = -1.5
        assert_equal(esperado, resultado, "test_factor_fibonacci_limite_2")

    def test_factor_fibonacci_limite_3(self):
        resultado: float = factor_fibonacci(20, 100, 200)
        esperado: float = 610.0
        assert_equal(esperado, resultado, "test_factor_fibonacci_limite_3")

    # Escenario: Entradas inválidas
    
    def test_factor_fibonacci_invalido_1(self):
        with self.assertRaises(ValueError):
            factor_fibonacci(0)

    def test_factor_fibonacci_invalido_2(self):
        with self.assertRaises(ValueError):
            factor_fibonacci(-5)

    def test_factor_fibonacci_invalido_3(self):
        with self.assertRaises(TypeError):
            factor_fibonacci("cinco", 1, 1)

    def test_factor_fibonacci_invalido_4(self):
        with self.assertRaises(TypeError):
            factor_fibonacci(5, "a", "b")

if __name__ == "__main__":
    unittest.main()



