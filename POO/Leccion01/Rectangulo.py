class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
area = Rectangulo(base, altura).calcularArea()

print(f'Area de rectangulo: {area}')
