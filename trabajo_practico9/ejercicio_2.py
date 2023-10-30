# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los
# siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo
# ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from Persona import Persona
from Cuenta import Cuenta

print('CREA UNA PERSONA\n')

name = input('INGRESE EL NOMBRE DE LA PERSONA: ')
age = int(input('INGRESE LA EDAD DE LA PERSONA: '))
dni = int(input('INGRESE EL DNI DE LA PERSONA: '))

person = Persona(name, age, dni)

amount = int(input('INGRESE CUANTO DINERO TIENE EN SU CUENTA: '))
account = Cuenta(person, amount)

option_list = [1, 2, 3, 4]

while True:
    print('\n------------BIENVENIDO A SU BANCO------------')
    print('\n1. Mostrar Datos')
    print('2. Ingresar Dinero')
    print('3. Retirar Dinero')
    print('4. Cerrar')

    option = int(input('\nDIGITE UNA OPCION: '))

    if option not in option_list:
        print('\nOPCION INCORRECTA, INTENTE NUEVAMENTE.')
    else:
        if option == 1:
            account.show_information()
        elif option == 2:
            amount_earn = int(input('\nCUANTO DINERO DESEAS INGRESAR? '))
            account.earn(amount_earn)
        elif option == 3:
            amount_take_out = int(input('\nCUANTO DINERO DESEAS RETIRAR? '))
            account.take_out(amount_take_out)
        elif option == 4:
            break
