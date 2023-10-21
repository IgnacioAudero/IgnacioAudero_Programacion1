# 9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve
# Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos
# que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente
# tenemos tres oportunidades para intentarlo.

from functions_tps import login

attempts = 3
while attempts != 0:
    print('----------INGRESE SU USUARIO Y CONTRASEÑA----------')
    user = input('Usuario: ')
    password = input('Contraseña: ')

    verify_login, attempts = login(user, password,attempts)

    if verify_login:
        print(f'\nBIENVENIDO! USTED PUDO INGRESAR Y LE QUEDARON {attempts} INTENTOS')
        break
    else:
        print('\nUSUARIO O CLAVE INCORRECTOS')
        if attempts != 0:
            print(f'Intente nuevamente, le quedan {attempts} intentos\n')
        else:
            print('Usted se quedo sin intentos.')