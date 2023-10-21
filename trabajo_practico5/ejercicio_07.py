# 7.	Crea una función que recibe una lista con valores numéricos y devuelve
# el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo
# y el mínimo, utilizando la función anterior.

from functions_tps import find_max_min

list_numbers = []

while True:
    how_numbers = int(input('Cuantos numeros vas a ingresar? '))
    if how_numbers <= 0:
        print('Error, valor no valido intente de nuevo.')
    else:
        break

for i in range(how_numbers):
    number = float(input(f'Ingrese el numero {i+1}: '))
    list_numbers.append(number)

number_max, number_min = find_max_min(list_numbers)

print(f'El valor maximo ingresado es {number_max}')
print(f'El valor minimo ingresado es {number_min}')