# 6.	Crea una lista de números y utiliza un bucle for para encontrar un número
# específico. Cuando encuentres el número, usa break para salir del bucle.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

serch_number = int(input('Ingrese el numero que se buscara en la lista: '))

for number in number_list:
    if serch_number == number:
        print(f'Se encontro el numero {serch_number}!!')
        print(f'Lista: {number_list}')
        break
else:
    print(f'No pudimos encontrar el numero {serch_number} en la lista')
    print(f'Lista: {number_list}')