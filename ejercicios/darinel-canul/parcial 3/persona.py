"""
crea una clase persona con los siguientes atributos: nombre, edad, genero y 
nacionalidad
Agrega un  metodo para imprimir los datos de la persona y otro metodo para calcular el 
Crea un objeto de la clase persona y utiliza los metodos para 
mostrar su informacion y calcula su año de nacimiento
"""
import datetime

class Persona:
    def __init__(self, nombre, edad, genero, nacionalidad = "mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad

    def imprimir_datos(self):
        print("-----informacion-----")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad, "años")
        print("Genero: ", self.genero)
        print("Nacionalidad: ", self.nacionalidad)

    def calcular_nacimiento(self):
        año_actual = datetime.datetime.now().year
        año_nacimiento = año_actual - self.edad
        return año_nacimiento
def main():
    objpersona = Persona("Marco Bonilla", 38, "masculino")
    objpersona.imprimir_datos()
    año_nacimiento = objpersona.calcular_nacimiento()
    print("Año de nacimiento: ", año_nacimiento)

if __name__ == "__main__":
    main()