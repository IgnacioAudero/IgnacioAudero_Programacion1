#EJERCICIOS EN CLASE

#Ejercicio 1

print('ENCRIPTAR MENSAJES USANDO EL METODO "LA CIFRA DEL CESAR"\n')

displace = int(input('Ingrese el numero de desplazamiento: '))

alphabet_tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O','P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z') #Alfabeto completo

for i in range(5):
  phrase_encrypt = ''

  phrase = input(f'INGRESE LA FRASE {i+1}: ').upper()

  for letter_phrase in phrase:

    if letter_phrase not in alphabet_tuple:

      phrase_encrypt = phrase_encrypt + letter_phrase

    for alphabet_index in range(len(alphabet_tuple)):

      if letter_phrase == alphabet_tuple[alphabet_index]:

        index_encrypt = alphabet_index + displace

        if index_encrypt >= len(alphabet_tuple):

          index_encrypt = (alphabet_index + displace) % 27

        phrase_encrypt = phrase_encrypt + alphabet_tuple[index_encrypt]
  
  print(f'Frase encriptada: {phrase_encrypt}')

print('-----------------------------------------------------------------------------------------------------------------------------------')

#Ejercicio 2

pair_total = 0
odd_total = 0

while True:
  number = int(input('Ingrese un numero entero positivo o ingrese 0 para salir: '))

  if number == 0:
    break

  while number < 0:

    number = int(input('Error. Tiene que ingresar un numero mayor a 0. Ingrese un numero nuevamente: '))
  
  number = str(number)
  counter_pair = 0
  counter_odd = 0

  for n in number:

    n = int(n)

    if n % 2 == 0:
      counter_pair = counter_pair + 1

    if n % 2 != 0:
      counter_odd = counter_odd + 1
  
  pair_total = pair_total + counter_pair
  odd_total = odd_total + counter_odd

  print(f'La cantidad de cifra/s par/es del numero {number} es: {counter_pair}')
  print(f'La cantidad de cifra/s impar/es del numero {number} es: {counter_odd}\n')


print(f'La cantidad total de numeros paes es: {pair_total}')
print(f'La cantidad total de numeros impares es: {odd_total}')