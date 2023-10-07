# 16-	Haz una calculadora básica pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# •	Si operación es 1 entonces debemos ver el resultado de a + b
# •	Si operación es 2 entonces debemos ver el resultado de a * b
# •	Si operación es 3 entonces debemos ver el resultado de a - b
# •	Si operación es 4 entonces debemos ver el resultado de a / b

print('\nCALCULADORA\n')
print('------------------MENU------------------')
print('1. SUMA')
print('2. MULTIPLICACION')
print('3. RESTA')
print('4. DIVISION\n')

option = int(input('Seleccione una opcion para realizar la operacion: '))

if option == 1:
    a = float(input('Valor del primer numero: '))
    b = float(input('Valor del segundo numero: '))
    result = a + b
    print(f'{a} + {b} = {result}')
elif option == 2:
    a = float(input('Valor del primer numero: '))
    b = float(input('Valor del segundo numero: '))
    result = a * b
    print(f'{a} * {b} = {result}')
elif option == 3:
    a = float(input('Valor del primer numero: '))
    b = float(input('Valor del segundo numero: '))
    result = a - b
    print(f'{a} - {b} = {result}')
elif option == 4:
    a = float(input('Valor del primer numero: '))
    b = float(input('Valor del segundo numero: '))
    if b == 0:
        print('No se puede dividir por 0.')
    else:
        result = a / b
        print(f'{a} / {b} = {result}')
else:
    print('Opcion no valida')