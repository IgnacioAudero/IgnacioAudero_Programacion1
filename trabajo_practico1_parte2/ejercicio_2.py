
#? 2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

import math

print('CALCULAR HIPOTENUSA DE UN TRIANGULO RECTANGULO.\n')

cathetus1 = float(input('Ingrese el primer cateto: '))
cathetus2 = float(input('Ingrese el segundo cateto: '))

hypotenuse = math.sqrt((cathetus1 ** 2) + (cathetus2 ** 2))

print(f'\nHIPOTENUSA = {hypotenuse}')