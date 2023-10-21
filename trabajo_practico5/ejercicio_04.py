# 4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

from functions_tps import multiple_number

print('INGRESAR DOS NUMEROS')

fst_number = int(input('Ingresar el primer numero: '))
scd_number = int(input('Ingresar el segundo numero: '))

is_multiple = multiple_number(fst_number, scd_number)       # Llamado a la funcion que evaluara si los numeros son multiplos

if is_multiple == 0:
    print(f'El primer numero ({fst_number}) es multiplo del segundo numero ({scd_number}).')
elif is_multiple == 1:
    print(f'El segundo numero ({scd_number}) es multiplo del primer numero ({fst_number}).')
elif is_multiple == -1:
    print('Los numeros ingresados no son multiplos entre si.')