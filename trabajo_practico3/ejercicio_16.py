# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba
# cuántos negativos ha introducido.

while True:
    how_much_numbers = int(input('Cuantos numeros desea ingresar? '))
    if how_much_numbers > 0:
        break
    else:
        print('Usted esta intentando ingresar una cantidad de numeros incorrecta. Intente de nuevo.')

how_much_negatives = 0

for i in range(1, how_much_numbers + 1):
    number = int(input(f'Ingrese el numero {i}: '))
    if number < 0:
        how_much_negatives += 1

print(f'La cantidad de numeros negativos ingresados es: {how_much_negatives}')