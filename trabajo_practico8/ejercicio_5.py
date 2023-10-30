# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista

from functions_tps import find_higher

numbers_list = []

while True:
    number = int(input('INGRESE UN NUMERO: '))

    numbers_list.append(number)

    print('DESEA CONTINUAR CARGANDO NUMEROS?')
    option = input('S/N: ')

    if option.upper() == 'N':
        break

print('\nLISTA DE NUMEROS INGRESADOS.')

for num in numbers_list:
    print(num, end = ' ')

higher = find_higher(numbers_list)

print(f'\nEL NUMERO MAYOR EN LA LISTA ES: {higher}')