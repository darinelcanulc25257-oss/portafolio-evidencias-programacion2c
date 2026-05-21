import unittest

from cuenta import Cuenta
from banco import Banco

class testInregracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = Cuenta("fulanito perez", "001", 1000)
        self.cuenta2 = Cuenta("fulanito perez", "001")

        self.banco =Banco()

    def test_transferencia_exitosa(self):
        resultado=self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "deberia realizarce de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "el saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta 2 deberia ser 350")

    def test_Transferencia_saldo_insuficientre(Self):
        resultado =Self.banco.transferir(Self.cuenta1, Self.cuenta2, 1200)
        Self.assertFalse(resultado, "La tranferencia no se deberia realizar al no disponer de saldo suficiente")
        Self.assertEqual(Self.cuenta1.saldo, 1000,"El saldo deberia mantenerse sin cambios")
        Self.assertEqual(Self.cuenta2.saldo, 0, "El saldo de la cuanta 2 deberia ser 0")