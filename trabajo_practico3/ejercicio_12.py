# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.

word = input('Ingrese una frase: ')
letter = input('Ingrese una letra y te dire cuantas veces esta en la frase: ')

if len(letter) > 1:
    print('Usted ingreso mas de una letra.')
else:
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    print(f'La letra {letter} aparece {counter} veces en la frase {word}')