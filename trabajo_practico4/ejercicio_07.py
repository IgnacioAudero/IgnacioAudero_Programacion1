# 7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza
# un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza
# break para salir del bucle (Mostrar un mensaje por cada opción elegida).

while True:
    print('MENU')
    print('1- Milanesas')
    print('2- Asado')
    print('3- Fideos')
    print('0- Salir')
    option = int(input('Seleccione una opcion: '))

    if option in [1, 2, 3]:
        if option == 1:
            print('Usted eligio Milanesas.')
        elif option == 2:
            print('Usted eligio Asado.')
        else:
            print('Usted eligio Fideos.')
    elif option == 0:
        print('Usted eligio salir, hasta luego!')
        break
    else:
        print('Opcion incorrecta.')