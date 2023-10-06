
#? 13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

print('INVERTIR NUMERO')

numb = int(input('Ingresar un numero de dos cifras: '))

numb = str(numb)

if len(numb) != 2:
  print('El numero ingresado no tiene dos cifras')
else:
  numb_inverted = numb[1] + numb[0]
  numb_inverted = int(numb_inverted)
  numb = int(numb)
  print(f'El numero {numb} invertido es {numb_inverted}')