# 10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario
# la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si
# tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

print('\nBIENVENIDO A LA SALA DE VIDEOJUEGOS!\n')

age = int(input('Hola buen dia! Dime tu edad porfavor: '))

if age > 0:
    if age < 4:
        print('Usted es menor de 4 años, puede pasar gratis!')
    elif age >=4 and age <= 18:
        print(f'Usted tiene {age} años, la entrada le cuesta $500')
    else:
        print('Como usted tiene mas de 18 años la entrada le cuesta $1000')
else:
    print('Edad erronea.')