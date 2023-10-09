# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo, de altura el número introducido.

height = int(input('Ingrese una altura para el triangulo rectangulo: '))

if height <= 0:
    print('Altura no valida.')
else:
    for i in range(1, height + 1):
        print('*' * i)