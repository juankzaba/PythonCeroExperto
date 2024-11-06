from colecciones.desempaquetado_tuplas import producto

print(f'*** Combinación Listas y Tuplas ***')

#Definir una lista que almacene tuplas de productos

productos = [
    ('POO1', 'Camisa', 20),
    ('POO2', 'Jeans', 30),
    ('POO3', 'Sudadera', 40)
]

#Imprimir información de cada producto y calcular precio total
precio_total = 0

print(f'Información de los productos')

for producto in productos:
    #print(producto)
    id, descripcion, precio = producto
    print(f' producto: ID:{id}, Descripción: {descripcion}, Precio: ${precio}')
    precio_total += precio
    print(f'Pecio total de los productos: ${precio_total}')