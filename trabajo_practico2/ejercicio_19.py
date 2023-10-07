# 19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe
# un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

pencil_numbers = int(input('Ingresar cuantos lapices vas a comprar: '))
price = 60

total_price = pencil_numbers * price

if pencil_numbers >= 1000:
    discount = total_price * 0.07
    discount_price = total_price - discount
    print(f'Llevando {pencil_numbers} el precio total es de ${total_price}, pero por llevar 1000 o mas lapices se le '
          f'hace un descuento del 7% (${discount}), el precio final es de ${discount_price}')
else:
    print(f'Llevando {pencil_numbers} el precio final es de ${total_price}')