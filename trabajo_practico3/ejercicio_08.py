# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo.

number = int(input('Ingrese la altura del triangulo: '))

if number <= 0:
    print('La altura no puede ser 0 o negativo.')
else:
    odd_numbers = []
    for i in range(1, number + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()