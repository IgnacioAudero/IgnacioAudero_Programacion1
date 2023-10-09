# ejercicio 1

x = 0

while x <= 30:
    if x in [4, 6, 10]:
        print(f'Se salto el valor {x} de x')
    else:
        print(f'El valor del bucle es: {x}')

    if x == 15:
        print("Se rompio la ejecucion del bucle cuando x valia:", x)
        break

    x += 1