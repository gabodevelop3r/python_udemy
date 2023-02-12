from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('Hp', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Hp', 15)

computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('ACER', 'bluetooth')
raton2 = Raton('ACER', 'bluetooth')
monitor2 = Monitor('ACER', 15)
computadora2 = Computadora('ACER', monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'bluetooth')
raton3 = Raton('Gamer', 'bluetooth')
monitor3 = Monitor('Gamer', 34)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

# print(orden1)

orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)