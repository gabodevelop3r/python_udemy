from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero'))

    if a == b:
        raise NumerosIdenticosException('números idénticos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Excepción - Ocurrió un error : {e}, {type(e)}')
except TypeError as e:
    print(f'Excepción - Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Excepción - Ocurrió un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución de bloque finally')
print(f'resultado : {resultado}')
print('continuamos')