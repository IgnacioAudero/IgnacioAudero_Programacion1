# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál
# fue el mayor número ingresado.
number_higher = 0
while True:
    number = int(input('Ingrese un numero entero positivo o ingrese 0 para salir: '))
    if number < 0:
        print('El numero ingresado es negativo, intente nuevamente.')
        continue
    elif number == 0:
        break

    if number > number_higher:
        number_higher = number


print(f'El mayor de todos los numeros ingresados es el {number_higher}')