# 3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los
# números impares desde 1 hasta ese número separados por comas.

number = int(input('Ingrese un numero positivo: '))

if number > 0:
    numb_odd = ''
    for numb in range(1, number + 1):
        if numb % 2 == 1:
            if numb_odd:
                numb_odd += ', '
            numb_odd += str(numb)
else:
    print('Debe ingresar un numero positivo.')

print(f'Los numeros impares entre el numero ingresado: {numb_odd}')