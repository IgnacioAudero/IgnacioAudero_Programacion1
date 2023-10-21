# 16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de
# ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.

from functions_tps import count_digit

number = int(input('Ingresar un numero entero: '))
digit = input('Igresar un digito a buscar el el numero anterior: ')

if len(digit) != 1 or not digit.isdigit():
    print('Usted no ingreso un digito')
else:
    answer = count_digit(number, digit)

    if answer != 0:
        if answer == 1:
            print(f'El digito {digit} aparece {answer} vez en el numero {number}')
        else:
            print(f'El digito {digit} aparece {answer} veces en el numero {number}')
    else:
        print(f'El digito {digit} no aparece en el numero {number}')