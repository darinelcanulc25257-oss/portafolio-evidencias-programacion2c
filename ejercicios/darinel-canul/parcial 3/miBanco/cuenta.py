from ast import main 
class Cuenta:
#constructorde la clase cuenta 

    def __init__(self, cliente, cuenta, saldo=0):
        """
    Constructor de la clase Cuenta

     args:
        cliente (str): Nombre del titular de la cuenta
        cuenta(str): Numero o identificador de la cuenta
        saldo (float): Saldo inicial de la cuenta, por defecto es 0
        """

        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """
        Realiza un deposito en la cuenta

        args:
        monto (float): La cantidada depositar

        return:
        None
        """
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False
    def retirar(self,cantidad):
        """
        Realiza un retiro en la cuenta

        args:
        monto (float): La cantidad a retirar

        return:
        bool: True si el retiro fue exitoso, False si no se pudo realizar el retiro
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False



