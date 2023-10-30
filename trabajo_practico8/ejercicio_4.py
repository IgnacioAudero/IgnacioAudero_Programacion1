# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad
# del numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.

from functions_tps import even
number = int(input('INGRESE UN NUMERO NATURAL: '))

if number >= 0:
    if even(number):
        print(f'{number} es un numero par!')
    else:
        print(f'{number} es un numero impar!')
else:
    print('\nTIENE QUE INGRESAR UN NUMERO MAYOR A 0')