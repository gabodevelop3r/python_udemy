# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')

# imprimir los numeros enteros del 0 al 5

# contador = 0
# maximo = 6
# while contador < maximo:
#     print(contador)
#     contador += 1
# else:
#     print('fin ciclo while')

# imprimir los numeros del 5 a 1 de manera descendente

# minimo = 1
# contador2 = 5
#
# while contador2 >= minimo:
#     print(contador2)
#     contador2-=1
# else:
#     print('fin del ciclo while')

# cadena = 'hola'
#
# for letra in cadena:
#     print(letra)
# else:
#     print('fin ciclo for')

# for letra in 'Holanda':
#     if letra == 'a':
#         print(f'letra encontrada {letra}')
#         break
# else:
#     print('fin ciclo for')

for i in range(6):
    if i % 2 != 0:
        continue

    print(f'valor : {i}')

else:
    print('Fin ciclo for')













