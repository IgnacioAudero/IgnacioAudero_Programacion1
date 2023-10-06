
#? 9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

price = float(input('Ingrese el motno total de la compra y le indicare cual es el precio final con el 15% de descuento: '))

final_price = price - (price * 0.15)

print(f'El precio final de su compra con el 15% de descuento es de {final_price}')