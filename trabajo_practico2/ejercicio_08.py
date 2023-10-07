# 8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere”
# y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”.
# Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

print('\nBIENVENIDO, INICIA SESION PARA INGRESAR A CAMELOT\n')

user = input('Usuario: ').lower()
password = input('Contraseña: ').lower()

if user == 'gwenevere' and password == 'excalibur':
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')