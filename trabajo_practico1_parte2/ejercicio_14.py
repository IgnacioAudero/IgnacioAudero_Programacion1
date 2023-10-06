
#? 14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

print('INTERCAMBIAR VARIABLES')

A = int(input('Ingrese un valor para la variable A: '))
B = int(input('Ingrese un valor para la variable B: '))

pivot = A
A = B
B = pivot

print(f'El valor de la variable A ahora es {A}')
print(f'El valor de la variable B ahora es {B}')