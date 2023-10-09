# 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

print('TABLAS DE MULTIPLICAR')

for numb1 in range(1, 11):
    print(f'TABLA DEL {numb1}')
    for numb2 in range(0, 11):
        result = numb1 * numb2
        print(f'{numb1} X {numb2} = {result}')