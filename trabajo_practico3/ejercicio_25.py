# 25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando
# todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

while True:
    number = int(input('Ingrese un numero entero positivo: '))
    if number < 0:
        print('El numero ingresado no es un entero positivo.')
    else:
        break

if number == 0:
    print(f'El factorial de {number} es 1')
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f'El factorial de {number} es {factorial}')