# 15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al
# finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

from functions_tps import calculate_factorial

total_numbers = 0
while True:
    number = int(input('Ingresar un numero o ingrese 0 para salir: '))

    if number == 0:
        break
    elif number < 0:
        print('Ingrese un numero entero positivo porfavor.\n')
        continue

    total_numbers += 1
    factorial = calculate_factorial(number)

    print(f'\nEl factorial de {number} es: {factorial}\n')

print(f'\nNumeros leidos en total: {total_numbers}')