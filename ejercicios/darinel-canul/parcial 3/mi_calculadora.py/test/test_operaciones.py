import unittest
from mi_calculadora.src.operaciones import suma, rest , multiplicacion, division 

class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(30, 30), 60)


    def test_resta(self):
        self.assertEqual(rest(5, 2), 3)


    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)


    def test_division(self):
        self.assertEqual(division(6, 2), 3)

    def test_resta_valores_negativos(self):
        self.assertEqual(rest(-5, -2), -3)

if __name__ == '__main__':
    unittest.main()