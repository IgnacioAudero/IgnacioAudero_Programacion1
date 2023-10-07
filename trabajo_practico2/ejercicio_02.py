# 2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.

computer_year_old = int(input('Ingrese cuantos años tiene su computadora: '))

if computer_year_old < 0:
    print('Error, tu computadora no puede tener años en numeros negativos.')
elif computer_year_old <= 2:
    print('Tu computadora es nueva!')
elif computer_year_old > 2:
    print('Tu computadora es vieja, cambiala!')