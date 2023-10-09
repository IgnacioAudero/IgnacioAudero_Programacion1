# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria
# de todos los números ingresados.

amount = 0
while True:
    number = int(input('Ingrese un numero entero o ingrese 0 para salir: '))
    amount += number
    if number == 0:
        break
print(f'La suma total de todos los numeros ingresados es de {amount}')