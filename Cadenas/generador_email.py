print('***GENERADOR DE EMAIL***')

#Nombre completo
nombre_completo = '  Juan Carlos Zabala Uribe  '
print(f'Nombre usuario{nombre_completo}')
#Normalizar nombre de usuario
nombre_normalizado = nombre_completo.strip()#Limpiamos espacios en blanco al inicio y al final
#Reemplazar los espacios en blanco por puntos
nombre_normalizado = nombre_normalizado.replace(' ', '.')
nombre_normalizado = nombre_normalizado.lower() # Convertir a mayusculas
print(f'Nombre de usuario personalizado: {nombre_normalizado}')

#DATOS DE LA EMPRESA

nombre_empresa = 'Soluciones Web y Digital'
print(f'\nNombre empresa: {nombre_empresa}')
extension_dominio = '.com.co'
print(f'Extensión de dominio {extension_dominio}')
#Quitamos espacios en blanco y convertimos a mayúsculas
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')
#Creamos email normal
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')
