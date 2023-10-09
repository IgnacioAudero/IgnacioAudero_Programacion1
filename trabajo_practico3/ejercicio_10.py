# 10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

number = int(input('Ingrese un numero entero: '))

if number <= 1:
    print(f'El numero {number} no es un numero primo.')
else:
    prime_number = True

    for i in range(2, number//2 + 1):
        if number % i == 0:
            prime_number = False
            break
    if prime_number:
        print(f'El numero {number} es numero primo!!')
    else:
        print(f'El numero {number} no es un numero primo.')