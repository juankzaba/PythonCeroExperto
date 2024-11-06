print(f'*** Operaciones con set ***')

a = {1,2,3,4}
b = {3,4,5,6}

union = a | b
print(f'Unión entre a y b: {union}')

interseccion = a & b
print(f'Interseción entre a y b: {interseccion}')

diferencia = a - b
print(f'Diferencia entre a y b: {diferencia}')