class Cubo:

    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular(self):
        return (self.ancho * self.profundo) * self.alto


ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proporciona el profundo: '))
cubo = Cubo(ancho,alto,profundo).calcular()

print(f'El calculo del volumen de un cubo: {cubo}')