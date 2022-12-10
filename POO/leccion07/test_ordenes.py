from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 50.1)

producto3 = Producto('calcetines', 03.23)
producto4 = Producto('Bluza', 14.23)

productos = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos)

orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

orden2 = Orden(productos2)
print(orden1)
print(f'Toral orden1: {orden1.calcular_total()}')
print(orden2)
print(f'Total orden2: {orden2.calcular_total()}')