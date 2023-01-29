class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


objeto1 = Persona('Juan', 13)
objeto2 = Persona('brito', 10)

print(objeto1 + objeto2)

print(objeto1 - objeto2)