# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye
# los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from Persona import Persona

print('CREA UNA PERSONA\n')

name = input('INGRESE EL NOMBRE DE LA PERSONA: ')
age = int(input('INGRESE LA EDAD DE LA PERSONA: '))
dni = int(input('INGRESE EL DNI DE LA PERSONA: '))

person = Persona(name, age, dni)
print()
person.show_datum()

if person.is_adult():
    print('\nLA PERSONA ES MAYOR DE EDAD.')
else:
    print('\nLA PERSONA NO ES MAYOR DE EDAD.')