# 1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y
# False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

from functions_tps import dni_validator


print('Bienvenido al validador de DNI')
dni = int(input('Ingrese su DNI porfavor (sin puntos): '))

is_dni = dni_validator(dni)     # Llama a la funcion para validar el DNI

if is_dni:      # Si la funcion retorna verdadero el DNI es valido, si retorna falso el DNI no es valido
    print('El DNI ingresado es valido!')
    print(f'DNI: {dni}')
else:
    print('El DNI ingresado no es valido.')