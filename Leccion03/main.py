# condicion = 'hola'
#
# if condicion == True:
#     print('Condicion Verdadera')
# elif condicion  == False:
#     print('Condicion falsa')
# else:
#     print('Condicion no reconocida')

# numero = int(input('Proporciona un valor entre 1 y 3: '))
#
# numeroTexto = ''
# if numero == 1:
#     numeroTexto = 'Numero uno'
# elif numero == 2:
#     numeroTexto = 'Numero dos'
# elif numero == 3 :
#     numeroTexto = 'Numero tres'
# else:
#     numeroTexto = 'Valor fuera de rango'
#
# print(f'Numero proporcionado: {numero} - {numeroTexto}')

# condicion = True
#
# print('Condicion Verdadera') if condicion else print('Condicion falsa')

# mes = int(input('Proporciona mes del año (1-12): '))
# estacion = None
#
#
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Verano'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'Otoño'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'Inverno'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'Primavera'
# else:
#     estacion = 'Mes incorrecto'
#
# print(f'Para el mes : {mes} la estacion es : {estacion}')


# edad = int(input('Proporciona tu edad: '))
# mensaje = None
# if 0 <= edad < 10:
#     mensaje = 'La infancia es increible'
# elif 10 <= edad < 20:
#     mensaje = 'Muchos cambios , mucho estudio'
# elif 20 <= edad < 30:
#     mensaje = 'Amor y comienza el trabajo'
# else:
#     mensaje = 'Estapa de vida no reconocida'
# print(f'Tu edad es: {edad} , {mensaje}')
#
#



"""
    Instrucciones de la tarea:
    El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
    El usuario proporciona un valor entre 0 y 10.
    Si esta entre 9 y 10 : imprimir una A
    Si esta entre 8 y menor a 9: imprimir una B
    Si esta entre 7 y menor a 8 : imprimir una C
    si esta entre 6 y menor a 7: imprimir una D
    si esta entre 0 y menor a 6: imprimir una F
    cualquier otro valor debe imprimir : Valor incorrecto
    Por ejemplo:
    Proporciona un valor entre 0 y 10:
    A

"""

calificacion = int(input('Proporciona un valor entre 0 y 10: '))
mensaje = None
if 9 <= calificacion <=10:
    mensaje = 'A'
elif 8 <= calificacion < 9:
    mensaje = 'B'
elif 7 <= calificacion < 8:
    mensaje = 'C'
elif 6 <= calificacion < 7:
    mensaje = 'D'
elif 0 <= calificacion < 6:
    mensaje = 'F'
else:
    mensaje = 'valor incorrecto'
print(mensaje)




