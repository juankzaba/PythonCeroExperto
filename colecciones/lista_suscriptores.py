print(f'*** Lista de Suscriptores ***')

suscriptores = {'luisa@mail.com','alejandr@mail.com','monica@mail.com'}
print(f'Lista de suscriptores: {suscriptores}')

#Verificar si un suscriptor está en la lista
nuevo_suscriptor = 'salome@mail.com'

if nuevo_suscriptor in suscriptores:
    print(f'El suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor ha sido agregado a la lista {nuevo_suscriptor}')
print(suscriptores)

#Eliminar suscriptor
suscriptor_eliminar = 'alejandr@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido elimado de la lista de suscriptores')
print(suscriptores)

#Cantidad total de suscriptores
print(f'La cantidad de suscriptores es: {len(suscriptores)}')

#Mostrar lista de suscriptores
print(f'-- Lista de suscriptores---')

for lista_suscriptores in suscriptores:
    print(f'-{lista_suscriptores}')