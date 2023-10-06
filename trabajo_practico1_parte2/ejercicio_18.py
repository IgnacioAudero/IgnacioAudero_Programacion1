
#? 18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

price = float(input('Ingrese cuanto costo la cena: '))

price_final = price + (price * 0.062) + (price * 0.1)

print(f'El costo final de la cena con el servicio y la propina incluida es de {price_final}$')