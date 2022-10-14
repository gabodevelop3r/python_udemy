operandoA = 3
operandoB = 2

suma = operandoA + operandoB
# print('Resultado suma:', suma)
print(f"Resultado suma: {suma}")

resta = operandoA - operandoB;
print(f"Resultado de la resta: {resta}")

multiplicacion = operandoA * operandoB
print(f"Resultado de la multiplicacion: {multiplicacion}")

division = operandoA / operandoB
print(f"Resultado de la division: {division}")

division = operandoA // operandoB
print(f"Resultado de la division (int): {division}")

modulo = operandoA % operandoB
print(f"Resultado residuo division (modulo): {modulo}")

exponente = operandoA ** operandoB
print(f'Resultado del exponente {exponente}')

"""
    El usuario debe proporcionar los valores de largo y ancho,
    y despues se debe imprimir el resultado en el siguiente formato
    (no usar acentos y respetar espacions, mayusculas , minisculas y saltos de linea):

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perimetro: <perimetro>

Las formulas para calcular el area y el perimetro de un Rectangulo son:
Area: alto*ancho
Perimetro: (alto+ancho)*2



alto = int(input('Proporciona el alto del rectangulo:'))
ancho = int(input('Proporciona el ancho del rectangulo:'))
area = alto * ancho
perimetro = (alto + ancho) * 2


print(f"Area: {area}")
print(f"Perimetro: {perimetro}")
"""
# Operadores de asignacion

miVariable = 10

miVariable = miVariable+1

#incremento con reasignacion
miVariable += 1

#decremento con reasignacion
miVariable -= 2
print(miVariable)
# multiplicacion miVariable = miVariable * 3
miVariable *= 3
print(miVariable)
# multiplicacion miVariable = miVariable / 2
miVariable /= 2
print(miVariable)

# Operadores de comparacion

a = 4
b = 2
resultado = (a == b)
print(f"resultado de comparar == : {resultado}")

resultado = a != b
print(f"resultado !=  : {resultado}")

resultado = a > b
print(f"resultado >  : {resultado}")

resultado = a >= b
print(f"resultado >=  : {resultado}")

resultado = a <= b
print(f"resultado <=  : {resultado}")

























