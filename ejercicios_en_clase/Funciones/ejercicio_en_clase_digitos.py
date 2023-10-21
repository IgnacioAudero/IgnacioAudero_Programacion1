import ejercicios_en_clase_functions

print('Ingrese numeros para sumar sus digitos, si usted ingresa 0 termina el programa.')
numbers_addition = 0

while(True):
    number = int(input('Ingrese el numero para sumar sus digitos: '))

    if number == 0:
        break
    else:
        numbers_addition += number
        print(f'La suma de los digitos es: {ejercicios_en_clase_functions.addition_digit(number)}')

print(f'La suma de todos los numeros ingresados es: {numbers_addition}')
print(f'La suma de los digitos de la suma de todos los numeros ingresados es: {ejercicios_en_clase_functions.addition_digit(numbers_addition)}')