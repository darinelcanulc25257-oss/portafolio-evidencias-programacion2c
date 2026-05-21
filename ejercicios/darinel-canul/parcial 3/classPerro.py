class Perro:
    #atributo de la clase perro
    especie = "Canis lupus familiaris"
    #constructor de la clase perro
    def __init__(self, nombre, raza= "caramelo", edad= 0):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    #metodos para imprimir los datos del perro
    def imprimir_datos(self):
        print("Nombre: ",self.nombre)
        print("Raza: " ,self.raza)
        print("Edad: ",self.edad, "años")
        print("Especie: ",self.especie)

def main():
    #crear un objeto de la clase perro
    perro1 = Perro("Firulais", "Labrador", 5)
    perro1.imprimir_datos()
    perro2 = Perro("Rex", "Pastor Alemán", 3)
    perro2.imprimir_datos()
    print("informacion del perro 2: ", perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("Max", "Bulldog", 2)
    perro3.imprimir_datos()
    perro4 = Perro( "Dante",)
    perro4.edad = 4
    perro4.imprimir_datos()
    perro2.raza = "pastor belga"
    perro2.imprimir_datos()
    perro5=Perro ("raya", "siames", 1)
    perro5.imprimir_datos()

if __name__ == "__main__":
    main()