# 7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

print('Introducir 3 numeros y dire cual es el menor de los 3.')

numb1 = int(input('Ingresar el primer numero: '))
numb2 = int(input('Ingresar el segundo numero: '))
numb3 = int(input('Ingresar el tercer numero: '))

smaller = numb1 #Suponemos que el numb1 es el mas chico

if numb1 > numb2:
    smaller = numb2
if numb1 > numb3:
    smaller = numb3

print(f'El menor de los 3 numeros ingresados es el {smaller}')