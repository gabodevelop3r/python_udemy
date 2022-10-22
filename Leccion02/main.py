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

miVariable = miVariable + 1

# incremento con reasignacion
miVariable += 1

# decremento con reasignacion
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

# a = int(input('escribe un valor numerico: '))
# if a % 2 == 0:
#     print(f'El valor de a {a} es par')
# else:
#     print(f'El valor de a {a} no es par')

# edadAdulto = 18
# edadPersona = int(input("Proporciona tu edad: "))
#
# if edadPersona >= edadAdulto:
#     print(f"La persona con edad {edadPersona} es un adulto")
# else:
#     print(f'La persona con edad {edadPersona} es menor de edad')

a = False
b = False

resultado = a and b
print('resultado', resultado)

resultado = a or b
print('resultado', resultado)

resultado = not a
print('resultado', resultado)

# valor = int(input('Escribe el valor: '))
# valorMinimo = 0
# valorMaximo = 5
#
# dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
#
# if dentroRango:
#     print(f'El valor {valor} esta dentro de rango')
# else:
#     print(f'El valor {valor} esta fuera de rango')



vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')

#
# edad = int(input('Introduce tu edad: '))
#
# veintes = edad >= 20 and edad < 30
# treintas = edad >= 30 and edad < 40
#
# if (20 <= edad < 30) or (30 <= edad < 40):
#     # print('dentro de rango (20\'s) o (30\'s)')
#     if veintes:
#         print('dentro de los 20\'s')
#     elif treintas:
#         print('dentro de los 30\'s')
# else:
#     print('No esta dentro de los 20\'s ni 30\'s')


"""
Instrucciones de tareas:
Solicitar al usuario dos valores , y determinar cual numero es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los numeros (la salida debe ser identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es: <numeroMayor>

"""
#
# numero1 = int(input('Proporciona el numero 1: '))
# numero2 = int(input('Proporciona el numero 2: '))
#
# if numero1 > numero2:
#     print(f'Numero 1 es mayor')
# else:
#     print(f'Numero 2 es mayor')



print('Proporcione los siguientes datos del libro')

libro = input("Proporciona el nombre: ")
id = int(input('Proporciona el ID: '))
precio = float(input('Proporcione el precio: '))
envio = input('Indica si el envio es gratuito (True/False)')


if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir (True/False)'

print(f'''
    Nombre: {libro},
    ID: {id},
    Precio: {precio},
    Envio: {envio}
    
''')


















































