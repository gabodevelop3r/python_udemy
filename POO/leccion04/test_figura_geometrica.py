from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica

print('Creacion objeto cuadrado'.center(50,'-'))
cuadrado = Cuadrado(lado=2, color='Rojo')
cuadrado.alto = 9
cuadrado.ancho = 9

print(f'Calculo del area del cuadrado {cuadrado.calcular_area()}')


# MRO = Method resolution order
print(Cuadrado.mro())

print(cuadrado)
print('Creacion objeto rectangulo'.center(50,'-'))
rectangulo = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo.ancho = 15

print(f'Calculo area rectangulo : {rectangulo.calcular_area()}')
print(rectangulo)