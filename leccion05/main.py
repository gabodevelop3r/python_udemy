nombres = ['Juan', 'Carla', 'Ricardo', 'Maria']

#imprimir la lista de nombres

print(nombres)

#acceder a los elementos de manera individual
print(nombres[2])

#acceder a los elementos de manera inversa
print(nombres[-1])

#imprimir un rango
print(nombres[0:2]) # sin incluir el indice 2

# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

# desde el indice indicado hasta el final
print(nombres[1:])

# cambiar un valor
nombres[3] = 'ivone'
print(nombres)

# iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print('fin ciclo for')

# preguntar el largo de una lista
print(len(nombres))

# agregar un elemento
nombres.append('Lorenso')
print(nombres)

# insertar un elemento en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# remover un elemento
nombres.remove('Octavio')
print(nombres)

# remover el ultimo valor agregado
nombres.pop()
print(nombres)


# eliminar un elemento de un indice
del nombres[0]
print(nombres)

# limpiar la lista
nombres.clear()
print(nombres)

# borrar la lista por completo
del nombres



# sintaxis de range (inicin <opcional>, fin <requerido>, incremento<opcional>)


# ejercicio 1. iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3

for i in range(11):
    if i % 3 == 0:
        print(f'es reato de 3 : {i}')
else:
    print('fin for')

# Ejercicio 2. crear un rango de numeros de 2 a 6 e imprimelos

for rango in range(2, 7):
    print(f'rango de 2 en 2: {rango}')
else:
    print('fin for')

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

for rango in range(3,11, 2):
    print(f'rando de 3 en 3 : {rango}')
else:
    print('fin for')


# definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
# saber el largo
print(len(frutas))

# acceder a un elemento
print(frutas[-1])

# acceder a un rango
print(frutas[0:1])

# recorrer elementos

for fruta in frutas:
    print(fruta, end= ' ')

# cambiar valor tupla
# frutas[0] = 'Pera'

frutasLista = list(frutas)
frutasLista[0] = 'pera'

frutas = tuple(frutasLista)

print('\n',frutas)
# eliminar tupla
del frutas


# dada la siguiente tupla
# crear una lista que solo incluya los numeros menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento);
else:
    print(lista)

# set
planetas = {'Marte', 'Jupiter', 'Venus'};
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento esta presente
print('Marte' in planetas)

# agregar un elemento
planetas.add('Tierra')
print(planetas)

# no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

# eliminar elementos posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)

#eliminar un elelemnto sin arrojar error
planetas.discard('Jupiter')
print(planetas)

# limpiar set
planetas.clear()
print(planetas)

# eliminar set
del planetas


# dict (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object oriented programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

# largo
print(len(diccionario))

# acceder a un elemento (key
print(diccionario['IDE'])
print(diccionario.get('OOP'))
# modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# recorrer los elementos de un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eleminar el diccionario
del diccionario














