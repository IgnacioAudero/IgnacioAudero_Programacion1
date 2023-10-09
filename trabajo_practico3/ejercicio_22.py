# 22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos
# que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números
# ingresados por el usuario fueron números pares.

amount_even = 0
while True:
    number = int(input('Ingrese un numero entero positivo o ingrese -1 para salir: '))
    if number == -1:
        break
    elif number < -1 or number == 0:
        print(f'El numero {number} no es un entero positivo. Intente nuevamente.')
        continue

    number_str = str(number)
    amount = 0

    for i in number_str:
        amount += int(i)

    print(f'La suma de los digitos del numero {number} es {amount}')

    if number % 2 == 0:
        amount_even += 1

print(f'\nCantidad de numeros pares ingresados -> {amount_even}')