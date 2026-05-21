class ave:
    def __init__(self, color="verde"):
        self.color = color

    def volar(self):
        print("puedo volar")

class canario(ave):
    def __init__(self, nombre, color="amarillo"):
        super().__init__(color)
        self.nombre = nombre

    def informacion(self):
        pass

canario = canario("amarillo", "fulanito")
print(canario.color)