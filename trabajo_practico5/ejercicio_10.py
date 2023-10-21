# 10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un
# diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del
# carrito  y devolver el precio final de la compra.

from functions_tps import calculate_discounts

print('BIENVENIDO A TU CARRITO DE COMPRAS\n')
shopping_cart = {}
while True:
    price = float(input('Ingrese el precio el producto: '))
    if price <= 0:
        print('El precio no puede ser 0 o negativo, intente nuevamente.\n')
        continue

    discount = float(input('Ingrese el descuento que tiene el producto: '))
    if discount < 0 or discount > 100:
        print('El descuento no puede ser menor a 0 ni mayor a 100, intente nuevamente.\n')
        continue

    shopping_cart[price] = discount

    print('')
    option = input('Desea cargar algun producto mas? (S/N): ')
    print('')

    if option.upper() == 'N':
        break

final_price = calculate_discounts(shopping_cart)

print(f'El precio final de la compra con los descuentos calculados es de ${final_price}')