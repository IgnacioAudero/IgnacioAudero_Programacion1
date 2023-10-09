# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta
# atrás desde ese número hasta cero separados por comas.

number = int(input('Ingrese un numero positivo: '))

if number > 0:
    countdown = ''
    for numb in range(number, -1, -1):
        if countdown:
            countdown += ', '
        countdown += str(numb)
else:
    print('Debe ingresar un numero positivo.')

print(f'Cuenta regresiva: {countdown}')