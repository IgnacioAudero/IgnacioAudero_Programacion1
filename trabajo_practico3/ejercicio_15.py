# 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

while True:
    number = int(input('Ingresar un numero mayor a 0: '))
    if number > 0:
        break
    else:
        print('El numero ingresado no es mayor a 0.')

for i in range(1, number + 1):
    if number % i == 0:
        print(f'El numero {number} es divisible por {i}')