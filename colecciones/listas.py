print('**Manejo de listas***')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista} -> Lista Original')

#Largo de la lista

print(f'Largo de la lista: {len(mi_lista)} ')

#Acceder a los elementos de la lista por índice

print(f'Accedemos al valor del indice 2: {mi_lista[2]}')
print(f'Accedemos al último índice de la lista: {mi_lista[-1]}')

#Modificar los elementos de una lista
mi_lista[0]=10
print(f'Modificamos el valor del índice 0: {mi_lista[0]}')

#Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'Nuevo elemento en la lista {mi_lista}')

#Añadir un nuevo elemento en un índice específico
mi_lista.insert(2, 15)
print(f'{mi_lista} se agrego el valor de 15 en el índice 2')

#Eliminar elemento de una lista
#Usando el método remove

mi_lista.remove(5)
print(f'{mi_lista} Se removió el valor 5 ')
#Removemos por índice por el método pop

mi_lista.pop(1) #Remueve el elemento del índice 1
print(f'{mi_lista} -> Se eliminó el índice 1')

#Eliminando usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el índice 2')

#Obtener sublistas
sublista = mi_lista[1:3] # Genera una sublista del índice 1 al 2 (3 no se incluye)
print(f'Sublista [1:3]: {sublista}')