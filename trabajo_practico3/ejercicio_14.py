# 14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y
# cuáles impares desde el primero hasta el segundo.

first_numb = int(input('Ingrese el primer numero: '))
second_numb = int(input('Ingrese el segundo numero: '))

start = min(first_numb, second_numb)
end = max(first_numb, second_numb)

print('Numeros pares.')
for numb in range(start, end + 1):
    if numb % 2 == 0:
        print(numb)

print('Numeros impares.')
for numb in range(start, end + 1):
    if numb % 2 != 0:
        print(numb)