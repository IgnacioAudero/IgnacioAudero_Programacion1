# 15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir
# entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo
# (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

import math

print('\nCALCULADOR DE AREA DE CIRCULO O TRIANGULO\n')
print('Introducir T o t si desea calcular el area del TRIANGULO')
print('Introducir C o c si desea calcular el area del CIRCULO')
option = input('Escriba una opcion: ').lower()

if option == 't' or option == 'c':
    if option == 't':
        base = float(input('Ingrese la base del triangulo: '))
        height = float(input('Ingrese la altura del triangulo: '))
        area = (base * height) / 2
        print(f"El área del triangulo es: {area}")
    else:
        radius = float(input('Ingresar el radio del circulo: '))
        area = math.pi * (radius ** 2)
        print(f"El área del círculo es: {area}")
else:
    print('Opcion incorrecta.')