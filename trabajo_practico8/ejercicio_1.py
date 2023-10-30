# 1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

from functions_tps import counter_digit

number = int(input('INGRESE UN NUMERO: '))

digits = counter_digit(number)

if digits != 1:
    print(f'El numero {number} tiene {digits} digitos.')
else:
    print(f'El numero {number} tiene {digits} digito.')