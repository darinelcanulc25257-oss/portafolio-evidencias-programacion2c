from banco import Banco 
from cuenta import Cuenta

def main():
    
    """MENU DEL PROGRAMA MI BANCO
    1. Aperturar nueva cuenta
    2. Ver clientes
    3. Depositar a cuenta
    4. Retirar de una cuenta
    5. Transferencie entre cuentas
    6. buscar cuenta
    7. Eliminar una cuenta
    8. salir del programa
    """
    def mostrar_menu():
        print("MENU DEL PROGRAMA MI BANCO")
        print("1. Aperturar nueva cuenta")
        print("2. Ver clientes")
        print("3. Depositar a cuenta")
        print("4. Retirar de una cuenta")
        print("5. Transferencie entre cuentas")
        print("6. buscar cuenta")
        print("7. Eliminar una cuenta")
        print("8. salir del programa")
    
    #Aperturar una cuenta
    banco = Banco()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuenta = Cuenta(nombre, numero_cuenta, saldo_inicial)
            banco.agregar_cuenta(cuenta)
            print("Cuenta creada exitosamente.")

        #Ver clientes
        elif opcion == "2":
            banco.mostrar_clientes()

        #Depositar a cuenta
        elif opcion == "3":
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta = banco.buscar_cuenta(numero_cuenta)
            if cuenta:
                cuenta.deposito(cantidad)
                print("Deposito realizado exitosamente.")
            else:
                print("Cuenta no encontrada.")

        #Retirar de una cuenta
        elif opcion == "4":
            numero_cuenta = input("Ingrese el numero de cuenta: ")
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta = banco.buscar_cuenta(numero_cuenta)
            if cuenta:
                if cuenta.retirar(cantidad):
                    print("Retiro realizado exitosamente.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Cuenta no encontrada.")

        #Transferencia entre cuentas
        elif opcion == "5":
            numero_origen = input("Ingrese el numero de cuenta de origen: ")
            numero_destino = input("Ingrese el numero de cuenta de destino: ")
            cantidad = float(input("Ingrese la cantidad a transferir: "))
            cuenta_origen = banco.buscar_cuenta(numero_origen)
            cuenta_destino = banco.buscar_cuenta(numero_destino)
            if cuenta_origen and cuenta_destino:
                if banco.transferir(cuenta_origen, cuenta_destino, cantidad):
                    print("Transferencia realizada exitosamente.")
                else:
                    print("Saldo insuficiente en la cuenta de origen.")
            else:
                print("Una o ambas cuentas no fueron encontradas.")


        #Buscar cuenta
        elif opcion == "6":
            numero_cuenta = input("Ingrese el numero de cuenta a buscar: ")
            cuenta = banco.buscar_cuenta(numero_cuenta)
            if cuenta:
                print(f"La cuenta es: {cuenta.nombre}, Saldo: {cuenta.saldo}")
            else:
                print("Cuenta no encontrada.")

        #Eliminar una cuenta
        elif opcion == "7":
            numero_cuenta = input("Ingrese el numero de cuenta a eliminar: ")
            if banco.eliminar_cuenta(numero_cuenta):
                print("Se elimino la cuenta.")
            else:
                print("No se encontro la cuenta.")  
        
        #Salir del programa
        elif opcion == "8":
            print("fin del programa")
            break       

if __name__=="__main__":
    main()
