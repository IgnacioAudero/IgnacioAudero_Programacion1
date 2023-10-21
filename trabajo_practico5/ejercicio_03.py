# 3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento
# mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en
# cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en
# un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad
# de letras del apellido y los 3 primeros dígitos de su DNI

from functions_tps import dni_validator, id_generator

while True:     # Bucle principal, se dejara de ejecutar cuando el usuario deje un espacio en blanco
    print('\nBIENVENIDO A SU CLUB!\nIngrese sus datos para obtener su identificador personal.\n')

    full_name = input('Ingrese su nombre/s y apellido (Si no deseas cargar mas datos dejar en blanco): ')

    if not full_name:       # Si el usuario deja en blanco la variable nombre completo corta el bucle
        break

    while True:     # Bucle para verificar que el nombre ingresado sea valido
        full_name_split = full_name.split()     # Dividir el nombre segun los espacios
        if len(full_name_split) == 3 or len(full_name_split) == 2:      # Si el nombre tiene mas de 3 palabras o menos de 2 corta el bucle, sino pide que ingrese el nombre nuevamente
            break
        else:
            print('\nNOMBRE INVALIDO.\nEl formato del nombre tiene que ser nombre segundo-nombre apellido, intente nuevamente.\n')
            full_name = input('Ingrese su nombre/s y apellido nuevamente (Si no deseas cargar mas datos dejar en blanco): ')

    while True:     # Bucle para verificar si el dni ingresado cumple los requisitos
        dni = int(input('Ingrese su DNI: '))
        is_dni = dni_validator(dni)     # Llamado a la funcion que evaluara si el dni tiene 7 u 8 numeros

        if not is_dni:      # Segun lo retornado de la funcion se valida si el dni es valido o no, si es valido corta el bucle
            print('\nDNI INVALIDO.\nSu DNI tiene que tener 7 u 8 numeros, intente nuevamente\n')
            continue
        else:
            break

    new_id = id_generator(full_name, full_name_split, dni)      # Llamado a la funcion que genera el id personalizado

    print(f'ID -> {new_id}')