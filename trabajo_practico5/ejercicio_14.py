# 14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando
# una función booleana que lo decida.

from functions_tps import prime_number

number = int(input('Ingrese un numero entero: '))

is_prime_number = prime_number(number)

if is_prime_number:
    print(f'\nEl numero {number} es un numero primo!')
else:
    print(f'\nEl numero {number} no es un numero primo.')