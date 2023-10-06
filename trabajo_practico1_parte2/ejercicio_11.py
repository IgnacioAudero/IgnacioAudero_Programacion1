
#? 11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

print('CALCULAR LA DISTANCIA ENTRE DOS NUMEROS')

number1 = float(input('Ingrese el primer numero: '))
number2 = float(input('Ingrese el segundo numero: '))

distance = abs(number1 - number2)

print(f'La distancia entre {number1} y {number2} es de {distance}')