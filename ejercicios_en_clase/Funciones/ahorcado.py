import ejercicios_en_clase_fc
import random

phrases_list = ['programacion', 'laboratorio', 'matematica', 'ingles', 'spd', 'algoritmos', 'funciones', 'bucles', 'condicionales']     # Lista de palabras
phrase = random.choice(phrases_list)     # Selecciona una palabra random de la lista y la guarda en una variable
phrase_hidden = ('_' * len(phrase))     # Reemplaza por guiones bajos las letras de la frase aleatoria

attempts = 4        # Cantidad de intentos fallidos que va a tener el usuario para adivinar la palabra

letters_input = []

print('BIENVENIDO AL AHORCADO\n')

while attempts != 0:
    print('PALABRA OCULTA')
    print(phrase_hidden)
    letter = input('\nIngrese una letra porfavor: ').lower()

    if letter in phrase:        #  Evalua si la letra se encuentra dentro de la frase aleatoria
        print(f'\nLa letra {letter} esta en la frase!\n')

        if letter in letters_input:     # Evalua si el usuario ya ingreso la letra
            print('Usted ya ingreso esta letra, intente nuevamente.\n')
            continue
        else:
            letters_input.append(letter)

        phrase_hidden = ejercicios_en_clase_fc.replace_letter(phrase, phrase_hidden, letter)

        if '_' not in phrase_hidden:        # Si dentro de la variable frase oculta ya no encuentra ningun guion bajo significa que el usuario adivino la palabra, por ende muestra un mensaje de victoria y utiliza un break para cortar el ciclo
            print('\nFELICIDADES, GANASTE EL JUEGO!')
            print(f'LA FRASE ERA {phrase.upper()}')
            break
    else:       # Si la letra no esta dentro de la frase aleatoria, se resta un intento y muestra por pantalla los intentos restantes
        if letter in letters_input:     # Evalua si el usuario ya ingreso la letra
            print('Usted ya ingreso esta letra, intente nuevamente.\n')
            continue
        else:
            letters_input.append(letter)
            attempts -= 1
            print(f'\nLa letra {letter} no esta en la palabra')
            print(f'Intentos restantes: {attempts}\n')

    print('\nLETRAS INGRESADAS: ')
    print(letters_input, '\n')

    if attempts == 0:       # Antes de que el bucle vuelva a evaluar la condicion, si la variable intento es igual a 0 el programa muestra un mensaje de derrota y muestra cual era la frase oculta
        print('\nPERDISTE, TE QUEDASTE SIN INTENTOS!')
        print(f'LA FRASE ERA {phrase.upper()}')