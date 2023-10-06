
#? 4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print('PASAR DE GRADOS FAHRENHEIT A CELSIUS')

fahrenheit = float(input('Ingrese los grados fahrenheit: '))

celsius = (fahrenheit - 32) * 5 / 9

print(f'La temperatura ingresada pasada a grados Celsius es de {celsius} °C')