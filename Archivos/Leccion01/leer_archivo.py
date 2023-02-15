archivo = open('prueba.txt', 'r', encoding='utf8')

# print(archivo.read())

# leer algunos caracteres

# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas

# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo

# for linea in archivo:
#     print(linea)

# leer linear

# print(archivo.readlines())

# acceder a una linea de la lista

# print(archivo.readlines()[1])

# abrimos un nuevo archivo
# a = anexar informacion

archivo2 = open('copia.txt', 'a')
archivo2.write(archivo.read())

# print(archivo2.read())
archivo2.close()
archivo.close()
print('se ha terminado el proceso de leer')
