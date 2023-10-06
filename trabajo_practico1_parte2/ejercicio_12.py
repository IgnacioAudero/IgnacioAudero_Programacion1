
#? 12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

import math

print('INGRESAR UN NUMERO Y CALCULAR SU RAIZ CUADRADA Y RAIZ CUBICA')

number = float(input('Ingresar un numero: '))
if number <= 0:
  print('Debe ingresar un numero mayor que 0')
else:
  square_root = math.sqrt(number)
  cube_root = math.pow(number, 1/3)

print(f'La raiz cuadrada de {number} es {square_root}')
print(f'La raiz cubica de {number} es {cube_root}')