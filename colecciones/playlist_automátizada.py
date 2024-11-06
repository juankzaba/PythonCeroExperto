from colecciones.playlist import cancion

print(f'*** Playlist de canciones*** ')

#Se crea la lisa vacía
lista_reproduccion = []
numero_canciones = int(input('Cuántas canciones deseas agregar? '))

#Iteramos cada elemento de la lista para agregar uno nuevo

for indice in range(numero_canciones):
    cancion = input(f' Ingresa la canción {indice +1}: ')
    lista_reproduccion.append(cancion)


#Ordenar lista en orden alfabético
lista_reproduccion.sort()

#Mostrar lista de canciones
print(f'\n Lista de reproducción en orden alfabético: ')
print(lista_reproduccion)

#Mostrar la lista iterando sus elementos
print(f'\n Iteramos la Playlist')

for cancion in lista_reproduccion:
    print(f'- {cancion}')