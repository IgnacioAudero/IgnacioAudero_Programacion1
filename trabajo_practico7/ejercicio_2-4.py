# 2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en
# orden ascendente utilizando el método de ordenamiento de selección

from functions_tps import selection_sort, insertion_sort

word_list = []

while True:
    word = input('INGRESE UNA PALABRA: ')

    word_list.append(word)

    print('DESEA CONTINUAR CARGANDO PALABRAS?')
    option = input('S/N: ')

    if option.upper() == 'N':
        break

print('\nLISTA DE PALABRAS INGRESADAS.')

counter = 1
for word in word_list:
    print(f'{counter}) {word}')
    counter += 1

print('\nLISTA DE PALABRAS INGRESADAS ORDENADAS ALFABETICAMENTE POR SELECCION.')

word_list = selection_sort(word_list)

counter = 1
for word in word_list:
    print(f'{counter}) {word}')
    counter += 1

# 4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según
# su longitud. Puedes utilizar el método de ordenamiento de inserción.

print('\nLISTA DE PALABRAS INGRESADAS ORDENADAS SEGUN LONGITUD POR INSERCION.')

word_list = insertion_sort(word_list)

counter = 1
for word in word_list:
    print(f'{counter}) {word}')
    counter += 1