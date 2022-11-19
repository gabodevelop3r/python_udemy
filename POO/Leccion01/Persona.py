class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


print(type(Persona))


persona1 = Persona('Juan', 'Lara', 26, '23322332', 2, 3, 4, m='manzana', p='Pera')
print(persona1.mostrar_detalle())


# Persona.mostrar_detalle(persona1)

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()
