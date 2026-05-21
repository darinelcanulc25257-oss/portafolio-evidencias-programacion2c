import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):
    
    def setUp(self):
        self.cuenta = Cuenta("Fulanito Perez Mengano","001")

#--------prueba del constructor ----------------

    def test_validar_saldo_inicial(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial debe ser 0 por defecto")
    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito Perez Mengano", "El nombre del cliente no es valido")

#--------prueba del deposito ----------------
    def test_depositar_dinero_valido(self):
        resultado = self.cuenta.deposito(100)
        self.assertTrue(resultado, "El deposito no se realizo correctamente")
        self.assertEqual(self.cuenta.saldo, 100, "El saldo no se actualizo correctamente despues del deposito")