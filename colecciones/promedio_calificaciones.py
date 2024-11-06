print(f'*** Promedio de calificaciones +**')

total_calificaciones = int(input('Proporcione el numero de calificaciones a evaluar: '))
calificaciones = []

#Iteramos
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificación[{indice}]  = '))
    calificaciones.append(calificacion)

#Imprimir las califiaciones
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

#Calculo de promedio de calificaciones
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones

print(f'\npromedio de las calificaciones: {promedio:.2f}')


