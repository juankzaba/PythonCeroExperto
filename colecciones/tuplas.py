

print(f'*** Manejo de tuplas')

mi_tupla = (1,2,3,4,5,6)
print(mi_tupla)

#Iterar elementos de la tupla
for elemento in mi_tupla:
    print(elemento, end=' ')#end='' es para que queden en una sola línea

#Crear una tupla para una coordenada x,y
coordenada = (3,5)
print(f'\nCoordenada en el eje X: {coordenada[0]}')
print(f'Coordenada en el eje y: {coordenada[1]}')

#Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un elemento{tupla_un_elemento}')

#Tupla anidada
tupla_anidada = (1,(2,3),(4,5))
print(f'\nEsta es una tupla anidada: {tupla_anidada}')
print(f'\nEsta es una tupla anidada: {tupla_anidada[0]}')
print(f'\nEsta es una tupla anidada: {tupla_anidada[1]}')
print(f'\nEsta es una tupla anidada: {tupla_anidada[2]}')

#Acceder a los elementos de la tupla