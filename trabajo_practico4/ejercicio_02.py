# 2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.


print('BIENVENIDO A SU CUENTA BANCARIA')
money = 0
while True:
    print('-----------------------------------------------------------------')
    print('PARA DEPOSITAR\nD + (cantidad a depositar)')
    print('PARA RETIRAR\nR + (cantidad a retirar)')
    print('PARA FINALIZAR DEJAR ESPACIO EN BLANCO')

    bank_account = input('Ingrese que operacion desea hacer\n').upper()
    if bank_account in ['']:
        break

    split = bank_account.split()
    if len(split) != 2:
        print('-----------------------------------------------------------------')
        print('Formato de operacion no valido, intente nuevamente.')
        continue

    operation = split[0]
    amount = int(split[1])

    if operation == 'D':
        money += amount
        print(f'Se depositaron ${amount}')
        print(f'Saldo actual ${money}')
    elif operation == 'R':
        money -= amount
        print(f'Se retiraron ${amount}')
        print(f'Saldo actual ${money}')
    else:
        print('-----------------------------------------------------------------')
        print('Operacion no valida, intente nuevamente.')

print(f'En su cuenta bancaria hay ${money}')