# 5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura
# máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura
# máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

from functions_tps import temperature_median

print('CALCULAR TEMPERATURA MEDIA DE LOS DIAS\n')

while True:     # Bucle para validar que el usuario ingrese una cantidad de dias valida (no 0 ni numero negativo)
    days = int(input('Ingrese la cantidad de dias que desea calcular la temperatura media: '))
    if days <= 0:
        print('Cantidad incorrecta de dias, intente de nuevo.\n')
    else:
        break

while days != 0:        # Bucle que se repetira segun la cantidad de dias que ingrese el usuario
    max_temperature = float(input(f'Ingrese la temperatura maxima del dia {days}: '))
    min_temperature = float(input(f'Ingrese la temperatura minima del dia {days}: '))

    median = temperature_median(max_temperature, min_temperature)       # Llamado a la funcion que calcula la media entre la temperatura maxima y minima

    print(f'La temperatura media del dia {days} es de: {median}\n')

    days -= 1