# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo,
# replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

from functions_tps import duplicate_list

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

while True:
    duplicate = int(input('\nCUANTAS VECES DESEAS REPLICAR LOS ELEMENTOS DE LA LISTA? '))

    if duplicate > 0:
        break
    else:
        print('\nTIENES QUE INGRESAR UN NUMERO MAYOR O IGUAL A 1, INTENTE NUEVAMENTE.')

list_duplicate = duplicate_list(numbers_list, duplicate)

print(f'\nLISTA DE NUMEROS INGRESADOS DUPLICADOS {duplicate} VECES.')

for num in list_duplicate:
    print(num, end = ' ')