from colecciones.tuplas import mi_tupla

print(f'*** Manejo de conjuntos (sets) ***')

#Crear un conjunto
mi_set = {1,2,3,4,5,6}
print(f'Mi conjunto de elementos: {mi_set}')

#Agregar elementos al set
mi_set.add(7)

#Intentar agregar elemento ya existente
mi_set.add(4)#En el resultado no muestra nada porque ya existe en el conjunto
print(f'Conjunto modificado: {mi_set}')

#Eliminiar un elemento del conjunto
mi_set.remove(4)
print(f'Nuevo conjunto después del elemento eliminado: {mi_set}')

#Iterar elemento

for elemento in mi_set:
    print(elemento, end= ' ')

#Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 5 en el conjunto? {5 in mi_set}')

#Obtener la longitud del set
print(f'Longitud del conjunto: {len(mi_set)}')