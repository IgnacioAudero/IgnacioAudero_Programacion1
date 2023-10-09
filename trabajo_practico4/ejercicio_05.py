# 5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un
# bucle for. Utiliza la declaración continue para omitir los números impares.

for number in range(1, 21):
    if number % 2 != 0:
        continue
    else:
        print(number)