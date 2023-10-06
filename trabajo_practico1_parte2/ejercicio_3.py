
#? 3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

print('INGRESAR DOS NUMEROS Y MOSTRARE SU SUMA, RESTA, MULTIPLICACION Y DIVISION.\n')

number1 = int(input('NUMERO UNO: '))
number2 = int(input('NUMERO DOS: '))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print(f'SUMA = {addition}')
print(f'RESTA = {subtraction}')
print(f'MULTIPLICACION = {multiplication}')
print(f'DIVISION = {division}')