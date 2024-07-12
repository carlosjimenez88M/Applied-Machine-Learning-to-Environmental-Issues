class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}")

# Crear objetos
persona1 = Persona("Juan", 30, "Masculino")
persona2 = Persona("María", 25, "Femenino")
persona3 = Persona("Luis", 35, "Masculino")

# Mostrar información
persona1.mostrar_informacion()
persona2.mostrar_informacion()
persona3.mostrar_informacion()