# 23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce
# la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando
# el usuario ingrese el monto 0.
# 24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un
# nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las
# ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

amount = 0
while True:
    purchase = float(input('Ingresar el monto de su compra o ingrese 0 para salir: '))

    if purchase < 0:
        print('Monto no valido, intente nuevamente.')
    elif purchase == 0:
        break
    else:
        amount += purchase

if amount > 1000:
    amount_discount = amount - (amount * 0.1)
    print(f'Usted gasto ${amount}, por haber gastado mas de $1000 le haremos un descuento del %10')
    print(f'El monto total de las compras es de {amount_discount}')
else:
    print(f'El monto total de las compras es de ${amount}')

