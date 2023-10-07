# 5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
# informarle que no se puede procesar el dato.

char = input('Ingresar una letra y te dire si es vocal o es consonante: ').lower()

vocales = ('a', 'e', 'i', 'o', 'u')

if len(char) != 1:
    print('Error, usted ingreso mas de una letra')
else:
    if char in vocales:
        print(f'La letra "{char.upper()}" es una vocal!!')
    else:
        print(f'La letra "{char.upper()}" no es una vocal.')