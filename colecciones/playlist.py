from colecciones.iterar_listas import lista

print(f'*** Playlist de canciones*** ')

#Se crea la lisa vacía
lista_reproduccion = []

#Se agrega canciones
lista_reproduccion.append('Blinding Lights - The Weeknd')
lista_reproduccion.append('Levitating - Dua Lipa ft. DaBaby ')
lista_reproduccion.append('Dance Monkey - Tones and I ')

#Ordenar lista en orden alfabético
lista_reproduccion.sort()

#Mostrar lista de canciones
print(f'\n Lista de reproducción en orden alfabético: ')
print(lista_reproduccion)

#Ordenar lista en orden alfabético desendente
lista_reproduccion.sort(reverse=True)
#print(f'\n Lista de reproducción en orden alfabético desendente: ')
#print(lista_reproduccion)

#Mostrar la lista iterando sus elementos
print(f'\n Iteramos la Playlist')

for cancion in lista_reproduccion:
    print(f'- {cancion}')