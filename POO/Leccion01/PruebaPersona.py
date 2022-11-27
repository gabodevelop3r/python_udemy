from Persona import Persona

print('Creacion de objetos '.center(30, '_'))
persona1 = Persona('Carla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(30, '-'))
del persona1
