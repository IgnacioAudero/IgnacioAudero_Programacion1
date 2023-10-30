# 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe
# ingresar 0, el cual no debe guardarse.



numb_list = []
while True:
    numb = int(input('INGRESE UN NUMERO A GUARDAR EN UNA LISTA (ingrese 0 para salir): '))

    if numb == 0:
        break
    else:
        numb_list.append(numb)

# 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar
# su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

numb_del = int(input('\nINGRESAR UN NUMERO Y SI ESTA EN LA LISTA SE ELIMINARA: '))

not_del = True
for number in numb_list:
    if numb_del == number:
        numb_list.remove(number)
        not_del = False
        break
if not_del:
    print('NO SE ELIMINO NINGUN NUMERO!')

# 3.	Imprimir la sumatoria de todos los números de la lista.

numb_add = 0
for number in numb_list:
    numb_add += number

print(f'\nLa suma de todos los elementos de la lista es: {numb_add}')

# 4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean
# menores que el número dado. Imprimir esta nueva lista, iterando por ella.

other_numb = int(input('\nINGRESE OTRO NUMERO Y SE CREARA OTRA LISTA CON LOS NUMEROS MENORES PERTENECIENTES A LA LISTA ANTERIOR: '))
other_numb_list = [other_numb]

for number in numb_list:
    if number < other_numb:
        other_numb_list.append(number)

print('RESULTADO DE LA NUEVA LISTA')

for number in other_numb_list:
    print(number, end=' ')