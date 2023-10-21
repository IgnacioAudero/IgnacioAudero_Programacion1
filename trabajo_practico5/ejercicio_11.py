# 11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de
# aplicar la función dada a cada uno de los elementos de la lista.

from functions_tps import add_iva, calc_iva

print('BIENVENIDO, INGRESE EL COSTO DE SUS PRODUCTOS Y LE SUMARE EL IVA.\n')

price_products = []

while True:
    price = float(input('Ingrese el precio el producto: '))
    if price <= 0:
        print('El precio no puede ser 0 o negativo, intente nuevamente.\n')
        continue
    else:
        price_products.append(price)

    print('')
    option = input('Desea cargar algun precio mas? (S/N): ')
    print('')

    if option.upper() == 'N':
        break

price_iva_list = add_iva(price_products, calc_iva)

print('Precios sin iva:')

for price_no_iva in price_products:
    print(f'${price_no_iva}')

print('Precios con iva:')

for price_iva in price_iva_list:
    print(f'${price_iva}')