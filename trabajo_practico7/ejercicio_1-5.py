# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente
# utilizando el método de ordenamiento de burbuja.

from functions_tps import bubble_sort, bubble_sort_descending

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

print('\nLISTA DE NUMEROS INGRESADOS ORDENADOS POR BURBUJA.')

numbers_list = bubble_sort(numbers_list)

for num in numbers_list:
    print(num, end = ' ')

# 5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden
# descendente en lugar de ascendente.

print('\nLISTA DE NUMEROS INGRESADOS ORDENADOS DESCENDENTE POR BURBUJA.')

numbers_list = bubble_sort_descending(numbers_list)

for num in numbers_list:
    print(num, end = ' ')