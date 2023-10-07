# 13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
# Haciendo que el programa avise cuando se escriben valores negativos o nulos.

numb1 = int(input("Ingrese el primer número entero positivo: "))
numb2 = int(input("Ingrese el segundo número entero positivo: "))

if numb1 <= 0 or numb2 <= 0:
    print("Por favor, ingrese números enteros positivos.")
elif numb1 == numb2:
    print('Se ingresaron los mismos numeros')
else:
    if numb1 > numb2:
        higher = numb1
        lower = numb2
    elif numb1 < numb2:
        higher = numb2
        lower = numb1
    if higher % lower == 0:
        print(f"{higher} es múltiplo de {lower}.")
    else:
        print(f"{higher} no es múltiplo de {lower}.")