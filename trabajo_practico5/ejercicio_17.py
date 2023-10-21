# 17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número
# que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito
# e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar
# el factorial del mayor número ingresado.

from functions_tps import prime_number, addition_digit, count_digit, calculate_factorial

highest_number = 0
while True:
    number = int(input('\nIngresar un numero primo o un numero no primo para salir: '))

    is_prime = prime_number(number)

    if number > highest_number:
        highest_number = number

    if is_prime:
        addition_number = addition_digit(number)
        print(f'\nLa suma de los digitos del numero {number} es {addition_number}')

        while True:
            digit = input('\nIgresar el digito a buscar el el numero ingresado: ')

            if len(digit) != 1 or not digit.isdigit():
                print('Usted no ingreso un digito, intente nuevamente.')
            else:
                answer = count_digit(number, digit)
                if answer != 0:
                    if answer == 1:
                        print(f'El digito {digit} aparece {answer} vez en el numero {number}')
                        break
                    else:
                        print(f'El digito {digit} aparece {answer} veces en el numero {number}')
                        break
                else:
                    print(f'El digito {digit} no aparece en el numero {number}')
                    break
    else:
        factorial = calculate_factorial(highest_number)
        print(f'\nEl factorial de {highest_number} es: {factorial}')
        break