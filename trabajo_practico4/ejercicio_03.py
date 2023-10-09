# 3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números
# mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

prime_number = 0
is_prime_number = True
while True:
    number = int(input('Ingresar numeros mayores a 1 o ingresar 0 para salir: '))
    if number < 0:
        print('El numero ingresado debe ser mayor o igual a 1')
    elif number == 0:
        break

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime_number = False

    if is_prime_number:
        prime_number += 1

print(f'La cantidad de numeros primos ingresados es de {prime_number}')