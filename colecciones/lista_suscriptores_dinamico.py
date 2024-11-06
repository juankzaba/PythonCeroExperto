print(f'*** Lista de Suscriptores ***')

#Definimos conjunto inicial
suscriptores = set() #Definir conjunto vacío

numero_suscriptores = int(input(f'Proporciona el número de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores: {suscriptores}')

#Verificar si un suscriptor está en la lista
nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')

if nuevo_suscriptor in suscriptores:
    print(f'El suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor ha sido agregado a la lista {nuevo_suscriptor}')
print(suscriptores)

#Eliminar suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido elimado de la lista de suscriptores')
print(suscriptores)

#Cantidad total de suscriptores
print(f'La cantidad de suscriptores es: {len(suscriptores)}')

#Mostrar lista de suscriptores
print(f'-- Lista de suscriptores---')

for lista_suscriptores in suscriptores:
    print(f'-{lista_suscriptores}')