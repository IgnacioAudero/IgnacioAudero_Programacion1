name = input('Hola! Porfavor ingrese su nombre: ')

print(f'\nBIENVENIDO {name.upper()}')


while True:                             # Valida que el usuario ingrese una opcion correcta (1 o 2)
    print('MENU DE JUEGOS')
    print('1. Juego de números.')
    print('2. Juego de palabras.')

    option = int(input('\nSeleccione que juego desea jugar: '))

    if option == 1 or option == 2:      # Si el usuario ingresa 1 o 2 el bucle se corta
        break
    else:
        print('\nOpcion incorrecta, intente nuevamente.\n')


if option == 1:

    print(f'\n{name.capitalize()} seleccionaste JUEGO DE NUMEROS')

    average_odd = 0                 #  Esta variable almacena la suma de los numeros impares
    highest_even = 0                #  Esta variable almacena el mayor numero par ingresado
    odd_number_counter = 0          #  Esta variable cuenta cuantos numeros impares se ingresaron

    while True:                         #  Se le pide un numero al usuario hasta que ingrese el numero 0

        number = int(input('Ingrese un numero entero (para terminar el juego ingrese 0): '))

        if number == 0:
            break
        else:
            if number % 2 == 0:
                if number > highest_even:
                    highest_even = number       #  Si el numero ingresado es mayor que lo que se encuentra en la variable, el numero ingresado pasa a ser el mayor
            else:
                average_odd += number           #  Acumulador de los numeros impares
                odd_number_counter += 1         #  Contador de cuantos numeros impares se ingresaron

    number_average_odd = average_odd / odd_number_counter       #  Esta variable almacena el promedio de los numeros impares ingresados
    print(f'\n{name.upper()}, LOS RESULTADOS DEL JUEGO SON LOS SIGUIENTES')
    print(f'El mayor numero par es: {highest_even}')
    print(f'El promedio de los numeros impares es: {number_average_odd}')

else:

    print(f'\n{name.capitalize()} seleccionaste JUEGO DE PALABRAS')
    phrase = input('Ingrese una frase y te dire la cantidad de cada vocal que tiene la frase: ').lower()

    a_counter = 0           #
    e_counter = 0           #
    i_counter = 0           #  ESTAS VARIABLES CUENTAN CUANTAS VECES SE ENCUENTRA DICHA VOCAL DENTRO DE LA FRASE INGRESADA
    o_counter = 0           #
    u_counter = 0           #


    for letter in phrase:           #  Este bucle recorre la frase letra por letra
        if letter == 'a':           #  Estos condicionales comparan si la letra es una vocal y si lo es suma uno al contador de dicha vocal
            a_counter += 1
        elif letter == 'e':
            e_counter += 1
        elif letter == 'i':
            i_counter += 1
        elif letter == 'o':
            o_counter += 1
        elif letter == 'u':
            u_counter += 1

    print('La cantidad de cada vocal de la frase es:')
    print(f'A: {a_counter}')
    print(f'E: {e_counter}')
    print(f'I: {i_counter}')
    print(f'O: {o_counter}')
    print(f'U: {u_counter}')