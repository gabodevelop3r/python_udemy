def mi_funcion(nombre, apellido):
    print('saludos desde mi funcion')
    print(f'Nombre: {nombre} , Apellido: {apellido}')


mi_funcion('Juan', 'Perez')


def sumar(a: int = 0, b: int = 0) -> int:
    return a + b


print(f'Resultado sumar: {sumar(5, 3)}')


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Maria', 'Rose', 'Shina')
listarNombres('Laura', 'Carlos')

"""
    Crear una funcion para sumar los valores recibidos de tipo numerico,
    utilizando argumentos variables *args como parametro de la funcion
    y regresar como resultado la suma de todos los valores pasados como argumentos
"""


def sumarValores(*args: int) -> int:
    total = 0
    for valor in args:
        total += valor
    return total


print(f'total sumatoria: {sumarValores(10, 5, 6)}')

"""
    Crear una funcion para multiplicar los valores recibidos de tipo numerico
    utilizando argumentos variables *args como parametro de la funcion
    y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

"""


def multiplicarValores(*args: int) -> int:
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado


print(multiplicarValores(3, 5, 15))


def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')


listarTerminos(IDE='INTEGRATED DEVELOPMENT ENVIRONMENT', PK='PRIMARY KEY')


def desplegarNombres(nombres: list):
    for nombre in nombres:
        print(nombre)


desplegarNombres(['Juan', 'Carlos', 'Guillermo'])
desplegarNombres((10, 11))


def factorial(numero: int) -> int:
    if numero == 1:
        return 1
    elif numero <= 0:
        return None
    else:
        return numero * factorial(numero - 1)


factor = 0
print(f'El factorial de {factor} es : {factorial(factor)}')

"""
    Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
    Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5 , debe imprimir

    5
    4
    3
    2
    1
    
    En caso de pasar el valor de 3, debe imprimir
    3
    2
    1

"""


def imprimirDescendente(numero):
    if numero >= 1:
        print(f'{numero}')
        return imprimirDescendente(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor incorrecto')


imprimirDescendente(3)

"""
    Ejercicio : calculadora de impuestos
    Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
    # formula : pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

"""


# funcion que calcula el total de un pago incluyendo el impuesto
def calularTotalPago():
    pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
    impuesto = float(input('Proporcione el monto del impuesto: '))
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    print(f'Pago con impuesto: {pago_total}')


# calularTotalPago()


"""
    Ejercicio: convertidor de temperatura
    Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""


def convertidorTemperatura(grados: int, isCelsius: bool) -> int:

    if isCelsius:
        return (grados * 9/5) + 32
    else:
        return (grados - 32) / (9/5)


print(f'GRADOS FAHRENHEIT A CELSIUS: {convertidorTemperatura(86,False):0.2f}')
print(f'GRADOS CELSIUS A FAHRENHEIT: {convertidorTemperatura(32,True):.2f}')



